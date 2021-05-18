#!/usr/bin/python3
"""get subreddit subscribers"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ return sub count """
    subreddit_exists = requests.get(
        "https://reddit.com/r/{}".format(subreddit),
        headers={'User-agent': 'test'})
    if subreddit_exists.status_code == 200:
        subscribers = requests.get(
            "https://reddit.com/r/{}/about.json".format(subreddit),
            headers={'User-agent': 'test'})
        return (subscribers.json().get("data").get("subscribers"))
    else:
        return (0)
