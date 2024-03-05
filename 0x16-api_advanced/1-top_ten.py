#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def top_ten(subreddit):
    """
    returns the top ten hot posts for subreddit
    """
    domain = 'https://www.reddit.com'
    path = '/r/{}/hot.json'.format(subreddit)
    url = '{}{}'.format(domain, path)
    header = {
        'user-agent': '0x16-api_advanced:project/1.0 (by /u/samuelhetty)',
        'over18': 'yes'
    }
    response = requests.get(
        url,
        headers=header,
        allow_redirects=False
    )
    code = response.status_code
    if code >= 300:
        print('None')
    else:
        data = response.json().get('data')
        children = data.get('children')
        for child in range(10):
            hot_post = children[child].get('data')
            title = hot_post.get('title')
            print('{}'.format(title))
