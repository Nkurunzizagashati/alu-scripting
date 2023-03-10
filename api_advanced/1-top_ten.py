#!/usr/bin/python3
"""
Finding hot top 10 post
Finding hot top 10 post
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Myapi-app'}

    Args:
        subreddit (str): The name of the subreddit to get the top 10 hot
        posts for.

    Returns:
        None: If the subreddit is not valid, or if there was an error getting
        the subreddit data.
    """
    # Set the API endpoint URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set the request headers to include a User-Agent
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Make the API request and get the response
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        print("Error: Could not get subreddit data")
        return None

    # Extract the JSON data from the response
    data = response.json()

    # Get the list of posts
    posts = data['data']['children']

    # Print the titles of the first 10 posts
    for i in range(10):
        if i >= len(posts):
            break
        print(posts[i]['data']['title'])

    return None
