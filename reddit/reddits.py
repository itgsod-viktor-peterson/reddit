from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_hot = "https://oauth.reddit.com/r/{subreddit}/hot"

class Subreddit(object):

    def __init__(self, subreddit):
        self.subreddit = subreddit


    def hot(self):
        pprint(reddit.client.request(url_hot.format(subreddit=self.subreddit)))




