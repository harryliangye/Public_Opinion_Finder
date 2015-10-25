import tweepy


def TwitterMood(query, since_id):
#User authentication: Ye Liang(梁也)
    consumer_key="lFORZk7pmFwrojCqkOj82zEjd"
    consumer_secret="nTbFhinOXybnx5ISEShJPee9sn2JnWJ9MfhU7CygFC52fP5B2T"
    access_token="3502291578-kx4NrlwXNzf3offZwKmsrxMsgQK373IUKaHM754"
    access_token_secret="mT2S2ZQFhoWaD5Ennpe3L9CMsRliGeGb4BD4CLUm6tHGz"
#Application authentication: Public_Opinion_Finder
    API_KEY = "lFORZk7pmFwrojCqkOj82zEjd"
    API_SECRET = "nTbFhinOXybnx5ISEShJPee9sn2JnWJ9MfhU7CygFC52fP5B2T"
#--------------------------------authentication-------------------------#
    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#--------------------------------authentication-------------------------#
    (search_results, new_id) = NewTweets(api, query, since_id)
    return_set = []
    for tweet in search_results:
        encoded = str.encode(tweet.text, 'utf-8')
        return_set.append(encoded)
    return (return_set, new_id)

def NewTweets(api,query,since_id):
    try:
        if (since_id == 1):
            new_tweets = api.search(q=query, count=100)
        else:
            new_tweets = api.search(q=query, count=100, since_id = since_id)
        if (not new_tweets):
            return ([],0)
        new_id = new_tweets[-1].id
        return (new_tweets, new_id)
    except tweepy.TweepError as e:
    # Just exit if any error
        print("some error : " + str(e))
        return ([],-1)