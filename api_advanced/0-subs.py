#!/
usr/bin/python3
"""
    define function number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ number_of_subscribers """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    else:
        return 0
    
