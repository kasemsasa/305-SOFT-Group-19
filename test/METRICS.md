# Metrics Collection

[Google HEART framework](https://docs.google.com/presentation/d/15eCHSK0DUnF00R8eA2oMMlL9oRtyf8p_ZvA5GdR2UKw/edit?usp=sharing)

## Metrics

| Metric           | Description                          |
|------------------|--------------------------------------|
| NPS              | Net Promoter Score                   |
| Adoption         | Percentage of new users signing up   |
| DAU              | Daily Active Users                   |
| Retention        | Percentage of users returning        |
| CTR for completion of the Golden Path | Click-through rate for completing the primary user journey |
| Error Message Rate | Amount of error messages before reaching golden path |
| User Satisfaction Rate | Open-ended feedback from the users showing their satisfaction level with the app|
| Log-In Rate | The frequency with which users log in to their accounts within the app|
| Weekly Total Session Duration | The total duration of user sessions within the app over a one-week period|


## How to Collect
- **NPS**: Implement a user satisfaction popup at the end of the Golden Path asking users how likely they are to recommend the product. Record responses in the database.
- **Adoption**: Track authentication signups in Firebase.
- **DAU**: Record daily active users by tracking login events in Firebase.
- **Retention**: Calculate the percentage of users who return within a specified time frame (e.g., week, month) based on login activity.
- **CTR**: 
- **Error Message Rate**: Calculate the amount of error messages that occur before the user reaches the golden path screen.
- **User Satisfaction Rate**: Record data from surveys within the app that the users take to show their level of satisfaction when using the app.
- **Log-In Rate**: Track user login events each time a user successfully logs into their account.
- **Weekly Total Session Duration**: Start a timer when a user opens the app and stop it when the user closes the app or becomes inactive for a defined period (e.g., a few minutes).

