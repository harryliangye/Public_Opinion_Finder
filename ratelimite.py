import tweepy
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="lFORZk7pmFwrojCqkOj82zEjd"
consumer_secret="nTbFhinOXybnx5ISEShJPee9sn2JnWJ9MfhU7CygFC52fP5B2T"
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="3502291578-kx4NrlwXNzf3offZwKmsrxMsgQK373IUKaHM754"
access_token_secret="mT2S2ZQFhoWaD5Ennpe3L9CMsRliGeGb4BD4CLUm6tHGz"
API_KEY = "lFORZk7pmFwrojCqkOj82zEjd"
API_SECRET = "nTbFhinOXybnx5ISEShJPee9sn2JnWJ9MfhU7CygFC52fP5B2T"

if __name__ == '__main__':

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    new_tweets = api.search(q="how", count=100, lan = "en")
    limits = api.rate_limit_status()
    remain_search_limits = limits['resources']['search']['/search/tweets']['remaining']
    print(remain_search_limits)