#!/usr/bin/python3
""" prints hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of 10 hottest posts on subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the subreddit exists and handle non-200 status codes
        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data")

        if not data or "children" not in data:
            print("None")
            return

        # Print the titles of the hot posts
        children = data.get("children")
        for post in children:
            print(post.get("data", {}).get("title", "None"))

    except Exception as e:
        print("None")
