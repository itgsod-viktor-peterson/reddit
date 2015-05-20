from reddit  import client
from reddit.user import User
from reddit.reddits import Subreddit

bojohan = client.login('Victohry')

print bojohan.me()


python = Subreddit("python")
#
print python.hot()








