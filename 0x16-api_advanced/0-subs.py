#!/usr/bin/python3
"""Python Script that that queries Reddit API to return the number of subscribers"""
import json
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    user_agent = "reddit_user"

    headers = {"User-Agent": user_agent}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        return 0

    data = request.json()["data"]
    page_list = data["children"]
    page_data = page_list[0]["data"]

    return page_data["subreddit_subscribers"]