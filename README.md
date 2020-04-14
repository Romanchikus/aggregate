# WingTel Coding Challenge

## Requirements
* Python 3.7+
* Postgresql

## Challenge
Make a structure to collect user usage metrics, and to fetch small reports based on it.

We will have two types of usage - data usage and voice usage, 
i.e. how much users use internet traffic and how much they talked on a phone. 

Imagine that data for these metrics will be filled directly into database from a couple of
external sources(with raw sql), you just need to create structure.
Sources will make incrementing queries based on values already existing in db.

Expected data incoming rate - ~1000 updates per minute

Fields what can be sent from data usage services:

**Data usage incoming data fields:**

subscription id - ATTSubscription or SprintSubscription

price - numeric value, additional cost since last update

date - data will be per day based. so will just update data if usage for current day already exists.

kilobytes used - how much traffic used since last update, integer value

**Voice usage fields:**

subscription id - ATTSubscription or SprintSubscription

price - numeric value, additional cost since last update

date - data will be per day based. so will just update data if usage for current day already exists.

seconds used - how much seconds talked since last update, integer value

**NOTE**

Don't worry about storing data past two weeks old.

We have retention policy to wipe all data older two weeks, so tables won't grow infinitely.

You don't have to implement it. Just keep it in mind.


### Also we need to create purchase once users reaches some day limit

You will need to create API to receive this limit

Find subscriptions what reached limit of price on data and/or voice(not sum)

Subtract this amount from price in usage table

Optimize this query as much as possible, it's going to run quite often

Send back subscription ids and type of usage what exceeded a limit

Our agent will manually create purchases with limit price for these subs

```
[
    {
        "subscription_id": 1,
        "usage_type": "data"
    },
    {
        "subscription_id": 2,
        "usage_type": "voice"
    }
    {
        "subscription_id": 3,
        "usage_type": "data, voice"
    }
]
```


### also 
we want to fetch data usage metrics  and voice usage metrics separately 

by subscription, write an API for it

list of dict should be returned :

```
[{
'date':
'price':
'seconds_used' or 'kilobytes_used' 
}]
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### BONUS

### As agent can make a mistake, we want to validate it.
If user asks us why he paid so much for his subscription,

we need to validate price and kilobytes/seconds data sometimes.

write an API to check is everything is correct by subscription id

True or False should be returned(valid/invalid)

```
{
   "result": "valid"
}
```
```
{
    "result": "invalid"
}
```

Optimize this query as much as possible
