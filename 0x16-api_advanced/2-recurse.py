#!/usr/bin/python3
"""Queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    a recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-user-agent/0.1"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        after = data.get("data").get("after")

        for post in posts:
            hot_list.append(post["data"]["title"])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
