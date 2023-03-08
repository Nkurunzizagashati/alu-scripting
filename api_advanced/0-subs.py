#!/usr/bin/python3
"""
    lets bring requests, and json functions
    to our work space
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
        this function takes:
        1 arg : str (which is the name of
                a subreddit
        it returns the number of subscribers to
        that specific subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    else:
        return 0
    
