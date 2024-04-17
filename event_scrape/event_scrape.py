import feedparser
import json
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, initialize_app, db
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk

nltk.download('punkt')
tokenizer = AutoTokenizer.from_pretrained("fabiochiu/t5-base-tag-generation")
model = AutoModelForSeq2SeqLM.from_pretrained("fabiochiu/t5-base-tag-generation")

# Initialize Firebase Admin SDK
cred = credentials.Certificate("event_scrape/firebase/soft-group-19-firebase-adminsdk-z8wjf-5162254013.json")
initialize_app(cred, {
    'databaseURL': 'https://soft-group-19-default-rtdb.firebaseio.com/'
})

tags = []

def tag_content(content):
    inputs = tokenizer([content], max_length=512, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=10,
                            max_length=64)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    tags = list(set(decoded_output.strip().split(", ")))

    return tags

def fetch_rss_data():
    # Parse the RSS feed
    feed = feedparser.parse("https://urinvolved.uri.edu/events.rss")

    # Prepare response data
    events = []
    for item in feed.entries:
        event = {
            'link': item.link,
        }
        events.append(event)

    return {'events': events}

def delete_all_events():
    try:
        ref = db.reference('events')
        ref.delete()
        print("\nAll event info deleted from Firebase.\n-------------------------------------")
    except Exception as e:
        print(f"An error occurred while deleting event info from Firebase: {e}")

def write_to_firebase(event_info, index):
    try:
        if event_info is None:
            print("Event info is None.")
            return

        ref = db.reference('events')  # Reference to 'clubs' node in your Firebase Realtime Database

        event_details = event_info.get('preFetchedData', {}).get('event', {})

        name = event_details.get('name', '')
        id = event_details.get('id', '')
        organization_id = event_details.get('organizationId', '')

        # Extract image server base URL and profile image path
        image_server_base_url = event_info.get('imageServerBaseUrl', '')
        profile_image_path = event_details.get('imagePath', '')
        profile_image_url = f"{image_server_base_url}/{profile_image_path}"

        description_html = event_info['preFetchedData']['event']['description']
        soup = BeautifulSoup(description_html, 'html.parser')
        description_text = ''
        description_text = soup.get_text(strip=True)

        start_time = event_details.get('startsOn', '')
        ends_on = event_details.get('endsOn', '')

        benefits = event_details.get('benefits', '')

        # Extract address information if available
        address_info = event_details.get('address', {})
        if address_info:
            address_name = address_info.get('name', '')
            address = address_info.get('address', '')
        else:
            address_name = ''

        # Extract categories/tags if available
        tags = []
        categories = event_details.get('categories', [])
        for category in categories:
            tags.append(category.get('name', ''))

        tags.append(event_details.get('theme', ''))

        # Print loading message
        print("Writing data to Firebase...")

        # Create a dictionary with the extracted fields
        data = {
            "image_url": profile_image_url, 
            "id": id,
            "organization_id": organization_id,
            "name": name,
            "description": description_text,
            "start_time": start_time,
            "ends_on": ends_on,
            "address_name": address_name,
            "address": address,
            "benefits": benefits,
            "tags": tag_content("Event name: " + name + ", " + "Event description: " + description_text + ", " + "Address name: " + address_name)
        }

        # Push the data dictionary to Firebase with manual key
        ref.child(str(index)).set(data)

        print("Data successfully written to Firebase.\n--------------------------------------")
    except Exception as e:
        print(f"An error occurred while writing to Firebase: {e}")

def scrape_json_data(url, index):
    try:
        # Make an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for invalid responses

        # Parse HTML content
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        # Find script tags containing JSON data
        script_tags = soup.find_all('script')

        # Iterate through script tags to find JSON data
        for script in script_tags:
            if 'initialAppState' in script.text:
                # Extract JSON data
                json_raw = script.text[25:-1]  # Remove unnecessary characters
                event_info = json.loads(json_raw)
                write_to_firebase(event_info, index)
                break

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

# Run the main logic
try:
    delete_all_events()
    # Call the fetch_rss_data function
    rss_data = fetch_rss_data()
    
    # Extract events from the fetched RSS data
    events = rss_data['events']
    
    # Print the links of each event
    index = 0
    for event in events:
        print(event['link'])
        scrape_json_data(event['link'], index)
        index += 1
except Exception as e:
    print(f"An error occurred: {e}")

# Print a message indicating success
print('Execution completed successfully!')
