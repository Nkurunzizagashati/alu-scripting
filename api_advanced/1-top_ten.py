#!/usr/bin/python3
"""
this code will print the top ten posts in a given subreddit
"""
import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, Allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json()['data']['children']
    for post in posts:
        print(post['data'['title'])
