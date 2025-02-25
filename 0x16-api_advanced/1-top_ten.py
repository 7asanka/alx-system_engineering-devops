#!/usr/bin/python3
"""Queries the Reddit API"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "custom-user-agent/0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
