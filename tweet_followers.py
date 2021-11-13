import os
import tweepy
import pandas as pd

consumer_key = os.environ.get('Twitter_API_Key')
consumer_secret = os.environ.get('Twitter_API_Key_Secret')
access_key = os.environ.get('Twitter_Access_Token')
access_secret = os.environ.get('Twitter_Access_Token_Secret')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

term = input()

def tweetfollow(word):
    tweets = api.search_tweets(q=word, result_type='popular', lang='en', count=5)
    DF = pd.DataFrame(columns=['tweet_no', 'screen_name', 'id'])
    i = 1

    for tweet in tweets:
        screen_name = tweet.user.screen_name
        id = tweet.user.id
        followers = api.get_followers(user_id=id, screen_name=screen_name, count=5)

        for follower in followers:
            follower_name = follower.screen_name
            follower_id = follower.id
            TWEET_follow = [i, follower_name, follower_id]
            DF.loc[len(DF)] = TWEET_follow

        i = i + 1

    filename = 'tweet_followers.csv'
    DF.to_csv(filename)
    return

tweetfollow(term)
