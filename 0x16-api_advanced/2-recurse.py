#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursively returns list of titles of hot posts on subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Brendabett@alx-holbertonschool"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit is invalid or response failed
    if response.status_code == 404:
        return None

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    # Collect titles of hot posts
    for child in children:
        hot_list.append(child.get("data").get("title"))

    # Check if there's another page
    after = data.get("after")

    # Recursively call the function if more pages are available
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list if hot_list else None
