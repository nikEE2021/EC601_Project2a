import os
import sys
import tweepy
import pandas as pd
import tweet_followers as tw

consumer_key = os.environ.get('Twitter_API_Key')
consumer_secret = os.environ.get('Twitter_API_Key_Secret')
access_key = os.environ.get('Twitter_Access_Token')
access_secret = os.environ.get('Twitter_Access_Token_Secret')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# Runs program as it should with string search term and integer number
def run_normal():
    tw.tweetfollow("usa",5)
    tw_df = pd.DataFrame(pd.read_csv(r'tweet_followers.csv'))
    assert tw_df.shape[0] != 0


# Runs program twice with different inputs to see if the result of the first
# function call can be recovered
def run_twice():
    tw.tweetfollow("GPU",5)
    tw.tweetfollow("brain",4)
    tweets = api.search_tweets(q="GPU", result_type='popular', lang='en', count=5)
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

    tw_df = pd.DataFrame(pd.read_csv(r'tweet_followers.csv'))
    assert DF == tw_df


# Runs a large number to see if that number of results will be loaded in
    pass
def run_big():
    tw.tweetfollow("mess",10000000000000000000000000000000000000000000000000000)
    tw_df = pd.DataFrame(pd.read_csv(r'tweet_followers.csv'))
    n = tw_df.shape[0]
    assert 50000000000000000000000000000000000000000000000000000 == n


# All tests completed without errors
