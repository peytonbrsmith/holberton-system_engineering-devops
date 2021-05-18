#!/usr/bin/python3
""" get subreddit hot posts """
import json
import requests
import sys

def top_ten(subreddit):
    """ return sub count """
    subreddit_exists = requests.get(
        "https://reddit.com/r/{}".format(subreddit),
        headers={'User-agent': 'test'})
    if subreddit_exists.status_code == 200:
        hot_posts_req = requests.get(
            "https://reddit.com/r/{}/hot.json".format(subreddit),
            headers={'User-agent': 'test'})
        for post in list(hot_posts_req.json().get("data").get(
                "children"))[:10]:
            print(post.get("data").get("title"))
    else:
        print(None)
