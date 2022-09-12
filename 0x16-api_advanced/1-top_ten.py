#!/usr/bin/python3
"""Prints titles of first 10 hot posts listed"""
import json
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "reddit_user"

    headers = {"User-Agent": user_agent}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        print("None")
    else:
        data = request.json()["data"]
        post_list = data["children"]

        for posts in post_list[0:10]:
            print(posts["data"]["title"])
