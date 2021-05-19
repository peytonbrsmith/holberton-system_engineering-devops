#!/usr/bin/python3
"""

returns a list containing the titles of all hot articles for a given subreddit

"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ returns a list containing the titles of
    all hot articles for a given subreddit """
    if count > 1 and after is None:
        return (hot_list)
    if after is None:
        subreddit_exists = requests.get(
            "https://reddit.com/r/{}".format(subreddit),
            headers={'User-agent': 'test'})
        if subreddit_exists.status_code == 200:
            first_hot = requests.get(
                "https://reddit.com/r/{}/hot.json?limit=100".format(subreddit),
                headers={'User-agent': 'test'})
            for post in first_hot.json().get("data").get("children"):
                hot_list.append(post.get("data").get("title"))
            after = first_hot.json().get("data").get("after")
            recurse(subreddit, hot_list, after, count + 1)
        else:
            return (None)
    else:
        next_hot = requests.get(
            "https://reddit.com/r/{}/hot.json?after={}&limit=100".format(
                subreddit, after),
            headers={'User-agent': 'test'})
        for post in next_hot.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        after = next_hot.json().get("data").get("after")
        recurse(subreddit, hot_list, after, count + 1)
    return (hot_list)
