from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_hot = "https://oauth.reddit.com/r/{subreddit}/hot"

class Subreddit(object):

    def __init__(self, subreddit):
        self.subreddit = subreddit


    def hot(self):
        #return all posts

        data = reddit.client.request(url_hot.format(subreddit=self.subreddit))


        firstpost = data['data']['children'][0]

        return Post(firstpost)

        #return firstpost


class Post(object):

    def __init__(self, data):
        #print data['data'].keys()
        #self.author = data['author']
        #self.selftext = data['selftext']

        self.data = data

    def author(self):
        return self.data['data']['author']

    def text(self):
        return self.data['data']['selftext']

    def title(self):
        return self.data['data']['title']






