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
| Error Message Rate | |
| User Satisfaction Rate | |

## How to Collect
- **NPS**: Implement a user satisfaction popup at the end of the Golden Path asking users how likely they are to recommend the product. Record responses in the database.
- **Adoption**: Track authentication signups in Firebase.
- **DAU**: Record daily active users by tracking login events in Firebase.
- **Retention**: Calculate the percentage of users who return within a specified time frame (e.g., week, month) based on login activity.