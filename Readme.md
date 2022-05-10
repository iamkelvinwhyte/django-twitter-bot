# Django Tweeter Scraper List Test project.

Django Automating Twitter Data in Python Using Tweepy and API Access.

## Initial Project setup

    Set up a Twitter account if you don’t have one already.
    Using your Twitter account, you will need to apply for Developer Access and then create an application that will generate the API credentials that you will use to access Twitter from Python.

    git clone https://github.com/iamkelvinwhyte/django-twitter-bot.git
    python -m venv venv
    pip install -r requirements.txt
    edit settings.json with your your  Twitter API keys 
    {
    "bearer_token" : "",
    "consumer_key" :"",
    "consumer_secret" : "",
    "access_token" : "",
    "access_token_secret" : ""
    }
    python manage.py runserver

## Request example:

http://127.0.0.1:8000/

## Response example:

![alt text](https://github.com/iamkelvinwhyte/django-twitter-bot/blob/main/Screenshot.png?raw=true)