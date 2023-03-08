#!/usr/bin/python3
"""
    a function that queries the Reddit API and 
    returns the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid
    subreddit is given, the function should return 0.
"""
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    else:
        return 0
    