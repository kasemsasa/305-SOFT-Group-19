A/B Test name: Phrasing of the Rating System
User Story Number: US6 
Metric: Happiness
Hypothesis: The specific way a request for a rating/feedback is said can affect a user's decision to rate/give feedback to the product. For instance, "Would it be okay for you to review this?" is kind, but may be a bit too passive, leading people to not rate or respond. "REVIEW THIS NOW!!!" Is way too rude, and may result in lower ratings. For the feedback, providing (optional) makes users realize they do not have to provide feedback, but that would also mean less users will feel inclined to do so. As such, you must determine the best way to prompt the user to provide feedback and a rating. 
Experiment: To test this, we first make multiple versions of the app, the only difference being how the rating page is worded. In the ratings table, we will provide an additional table, called version, and then we will measure which version has the most ratings, and which version has the highest ratings. We should get a nice combination of most ratings and highest ratings, but we should prioritize higher ratings over more ratings.
Variations:
    - "How would you rate your experience?"/"(Optional) Please Provide feedback explaining your rating:"
    - "How would you rate your experience?"/"(Optional) Provide feedback explaining your rating:"
    - "How would you rate your experience?"/"(Optional) Please Provide feedback:"
    - "How would you rate your experience?"/"Please Provide feedback explaining your rating:"
    - "How would you rate your experience?"/"Provide feedback explaining your rating:"
    - "How would you rate your experience?"/"Please Provide feedback:"
    - "Rate this App!"/"(Optional) Please Provide feedback explaining your rating:"
    - "Rate this App!"/"(Optional) Provide feedback explaining your rating:"
    - "Rate this App!"/"(Optional) Please Provide feedback:"
    - "Rate this App!"/"Please Provide feedback explaining your rating:"
    - "Rate this App!"/"Provide feedback explaining your rating:"
    - "Rate this App!"/"Please Provide feedback:"

---

A/B Test Name: Dark Mode Impact on User Engagement
User Story Number: (Assign a unique number that corresponds to your backlog of user stories or features, if applicable.)
Metric (from the HEART grid): Engagement – measured by daily active users and user time spent in the app.
Hypothesis: Users are currently engaging with the app with an average session time of X minutes. We believe that by introducing a dark mode, we will improve user engagement as it may reduce eye strain and make reading easier, especially in low-light conditions. This could lead to an increased time spent in the app per session. We expect to see at least a 10% increase in the average session duration for users who activate dark mode.
Setup: Utilize Firebase A/B testing capabilities to serve the dark mode feature to a randomized 50% of our user base.
Audience: A segment of the user base that has logged in at least once in the past month to ensure they are familiar with the current design.
Duration: Run the experiment for a minimum of 3 weeks to collect sufficient data across different times and days.
Tracking: Using Firebase Analytics, track the average session duration and frequency of sessions for users in both the control group (light mode) and the experiment group (dark mode).
Variations:
Control (A): The current light mode of the app.
Variant (B): An alternative design with a dark mode theme.
Design Work and Mockups: (Here, you would include mockups and designs of the dark mode interface. Since we're conceptualizing this plan, I can’t provide actual designs, but you would want diagrams that show the user interface changes between light and dark modes.)

---
A/B Test Name: Onboarding Flow Optimization
User Story Number: US-6
Metric (from the HEART grid): Adoption
Hypothesis:
Problem: The current onboarding flow has a high drop-off rate, with many users failing to complete the registration process.
Impact: Improving the onboarding experience could lead to increased user adoption, as more users successfully complete the registration process and begin using the app.
Hypothesis: By simplifying and streamlining the onboarding flow, we will improve user adoption rates by reducing the friction associated with registration. We expect to see at least a 15% increase in the number of users who complete the onboarding process and reach the app's main interface.
Setup:
Utilize Firebase A/B testing capabilities to test the optimized onboarding flow with a randomized 50% of our user base. The remaining 50% will serve as the control group and will experience the current onboarding flow.
Audience:
Target users who have installed the app but have not yet completed the registration process. These users are crucial for adoption metrics as they represent potential new users who are interested in the app but have not fully engaged with it yet.
Duration:
Run the experiment for a minimum of 4 weeks to capture variations in user behavior over different periods, including weekdays and weekends.
Tracking:
Using Firebase Analytics, track the completion rate of the onboarding process for users in both the control group (current onboarding flow) and the experiment group (optimized onboarding flow). Additionally, track the time taken to complete the onboarding process for both groups to ensure that the optimization does not inadvertently lengthen the process.
Variations:
Control (A): The current onboarding flow, which includes multiple steps and input fields.
Variant (B): An optimized onboarding flow with fewer steps and simplified input fields. This variation aims to reduce friction and encourage users to complete the registration process more quickly.
Design Work and Mockups:
Include mockups and designs of the optimized onboarding flow. Focus on highlighting the differences between the current and optimized flows, such as reducing the number of input fields, providing clearer instructions, and optimizing the layout for better usability.

---
## A/B Test Name
Feature Engagement Experiment

## User Story Number
TBD

## Metric (from the HEART grid)
Retention

## Hypothesis
### Problem
Analysis reveals that a considerable portion of users show low engagement levels with core features shortly after onboarding.
### Impact
Improving feature engagement shortly after onboarding could lead to higher retention rates and increased user satisfaction.
### Hypothesis
By implementing an interactive tutorial showcasing key features immediately after login, users will have a better understanding of the app's value proposition, leading to improved retention rates.

## Experiment Setup
### Audience
Initially, allocate 40% of the user base to the experiment group, while the remaining 60% serves as the control group. This split allows for a significant experimental sample while minimizing potential negative impacts on the majority of users.
### Experiment Details
- **Experimental Group:** Upon successful login, users will be guided through an interactive tutorial highlighting core features through tooltips and guided interactions.
- **Control Group:** Users will experience the standard onboarding flow without the additional tutorial.

## Tracking using Firebase Analytics
1. **Log-In Rate:** Track successful login events for both experimental and control groups.
2. **Weekly Total Session Duration:** Monitor session durations for users in both groups to understand how engagement levels change over time.
3. **Retention:** Calculate retention rates for both groups over a specified time frame (e.g., weekly or monthly), based on login activity.

## Variations
### Design Variation
- **Experimental Group:** Users encounter a series of tooltips upon login, guiding them through key features. Each tooltip highlights a specific feature with a brief explanation and prompts the user to interact.
- **Control Group:** Users experience the standard login flow without any additional tooltips or guidance.

## Rationale
- The experimental design aims to improve feature comprehension and user engagement through interactive guidance.
- The control group ensures a baseline for comparison, allowing for accurate measurement of the experiment's impact.
- Utilizing Firebase Analytics facilitates precise tracking of metrics, enabling informed decision-making based on experiment outcomes.

## A/B Test Name:
Search Bar Placement Optimization
## User Story Number:
N/A
## Metric (grid):
Engagement: We will measure the engagement metric, specifically focusing on the number of searches performed by users during the testing period.
## Hypothesis:
We hypothesize that optimizing the placement of the search bar within the app will lead to increased user engagement with the search feature. By placing the search bar in a more prominent and accessible location, users will be more likely to utilize it to discover events and clubs, thus improving their overall experience with the app.
## Experiment:
We will conduct the experiment by testing two variations of the search bar placement:
## Variation A (Control):
Search bar placed at the top of the screen, adjacent to the app's title/logo.
All users will see this variation by default.
## Variation B (Experimental):
Search bar moved to the bottom of the screen, positioned within easy reach of the user's thumb.
50% of the user base will be randomly allocated to this variation to ensure a fair comparison.
Tracking Using Firebase Analytics:
To measure the success of the experiment, we will track the following metrics using Firebase Analytics:
**Number of Searches:** Track the total number of searches performed by users in both variations.

**Time Spent Searching:** Measure the average time users spend using the search feature in each variation.

**Search Result Click-through Rate:** Monitor the percentage of users who click on search results after performing a search in each variation.

## Variations:
Here are the proposed variations for the search bar placement:
Variation A (Control):

In this variation, the search bar is located at the top of the screen, providing users with easy access to initiate a search query. This placement is consistent with standard app design conventions.
Variation B (Experimental):

In this experimental variation, the search bar is moved to the bottom of the screen, making it more accessible for users with larger devices or those using one-handed navigation. This placement aims to enhance user convenience and encourage greater engagement with the search feature.
## Rationale:
The rationale behind testing the search bar placement is to optimize user experience and increase engagement with the search functionality. By comparing the two variations, we aim to identify the most effective placement that encourages users to utilize the search feature more frequently, leading to improved engagement metrics.
