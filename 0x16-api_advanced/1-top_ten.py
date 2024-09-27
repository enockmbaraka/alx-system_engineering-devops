#!usr/bin/python3
"""Function to print top 10 posts for Reddit subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of first 10 posts listed for subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10  # Limit the response to 10 posts
    }

    # Making the GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check for invalid subreddit or failed request
    if response.status_code != 200:
        print(None)
        return

    try:
        # Extracting data from JSON response
        data = response.json().get("data", {})
        children = data.get("children", [])

        # Check if there are no hot posts
        if not children:
            print(None)
            return

        # Print the title of each hot post
        for post in children:
            print(post.get("data", {}).get("title"))

    except ValueError:
        # Handle cases where the JSON response is invalid
        print(None)
