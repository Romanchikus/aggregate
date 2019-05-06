# WingTel Coding Challenge

## Requirements
* Python 3.5+
* SQLite

## Challenge
Create an endpoint that will allow a user to activate their own AT&T and/or Sprint subscription. This should include the following:

- Applies to any existing subscription with a status of `new`
- Changes the subscription status from `new` to `active`
- Creates an overdue purchase related to the subscription and the subscription's plan
- Checks for proper permissions
- Checks for required subscription data before activation, including `plan`, `phone_number`, `device_id`

*Note: The activation endpoint can be added to AT&T subscriptions, Sprint subscriptions, or both.*

## Bonuses
- Create a way to link a purchase directly to a subscription, not just a user.
- Improve and/or optimize the code
