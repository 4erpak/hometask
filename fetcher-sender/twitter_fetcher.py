#!/usr/bin/env python3
"""
Script to get data from the tweets with hashtag #DevOps
"""

from kafka import KafkaProducer
import tweepy
import json
import os

TOKEN = os.environ["twitter_bearer_token"]

client = tweepy.Client(bearer_token=TOKEN)

producer = KafkaProducer(bootstrap_servers=['kafka1:9092','kafka2:9093','kafka3:9094'],\
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

QUERY = '#DevOps -is:retweet -is:reply has:hashtags'

response = client.search_recent_tweets(query=QUERY,\
                                    user_fields=['username'],\
                                    tweet_fields=['id', 'entities'],\
                                    expansions=['author_id'] ,max_results=100)

tweets = response.data

includes = response.includes
users = includes["users"]

users = {user["id"]: user for user in users}

for tweet in tweets:
    d = {}
    d['Tweet ID'] = tweet.id
    d['Username'] = users[tweet.author_id].username

    tags = []
    for hashtag_record in tweet.entities["hashtags"]:
        tags.append(hashtag_record["tag"])
    d['Hashtags'] = tags
    producer.send('twitter', value = d)
    producer.flush()
