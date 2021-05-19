#!/usr/bin/python3
"""
2-main
"""
import sys
import requests

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
            x = 1
            for title in result:
                print(x, title)
                x = x + 1
        else:
            print("None")