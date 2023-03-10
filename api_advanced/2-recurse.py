#!/usr/bin/python3
"""
this code will fetch all the title for the hot posts in
a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    this function takes 3 parameters:
    subreddit:
                to specify the name of subreddit you want to deal with
    hot_list:
                to store the titles for hot posts

    after:
            to give us the last page we were on if there is other pages
            available
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    headers = {'User-Agent': 'Fab'}
    if after:
        url += '&after={}'.format(after)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        posts = res.json()['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = res.json()['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    return None
