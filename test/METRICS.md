@ -1,31 +1,34 @@
[Google HEART framework](https://docs.google.com/presentation/d/15eCHSK0DUnF00R8eA2oMMlL9oRtyf8p_ZvA5GdR2UKw/edit?usp=sharing)

<<<<<<< HEAD
### Metrics
- NPS
- Adoption
- DAU
- Retention 
- CTR
- Error Mesage Rate
- User Satisfaction Rating

=======
>>>>>>> 8767bb88d078acedfc6d21ade6a098307f73bd52
# Metrics Collection

[Google HEART Framework Presentation](link-to-google-slide)

## Metrics

| Metric           | Description                          |
|------------------|--------------------------------------|
| NPS              | Net Promoter Score                   |
| Adoption         | Percentage of new users signing up   |
| DAU              | Daily Active Users                   |
| Retention        | Percentage of users returning        |
| CTR for completion of the Golden Path | Click-through rate for completing the primary user journey |

## How to Collect
- **NPS**: Implement a user satisfaction popup at the end of the Golden Path asking users how likely they are to recommend the product. Record responses in the database.
- **Adoption**: Track authentication signups in Firebase.
- **DAU**: Record daily active users by tracking login events in Firebase.
- **Retention**: Calculate the percentage of users who return within a specified time frame (e.g., week, month) based on login activity.
<<<<<<< HEAD
- **CTR for completion of the Golden Path**: Track user clicks on each step of the Golden Path and calculate the completion rate.
-**User Satisfaction Rating**: When the app opens [when a user logs in, as opposed to signing up], a prompt appears, stating "on a scale of 1 to 5, how would you rate this app?" clicking sends the response using a cloud function, and afterward, the prompt states "*optional* please explain your response." The quantative response will also be sent via a different cloud function. 

=======
>>>>>>> a484a0a9e48337856618c37f887feee62dadf27b
