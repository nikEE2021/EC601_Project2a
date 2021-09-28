# EC601_Project2a

The file "tweet_followers.py" searches Twitter for five popular tweets related to the search term "GPU" and stores the user ID and screen name of five followers of the authors of the afformentioned tweets. This code is written in python 3.8.8 and uses the "tweepy" library to access two twitter API methods: "GET followers/list" and "GET search/tweets" which are invoked using the python functions "API.search_tweets()" and "API.get_followers()" respectively. The data is stored in a .csv file using the "pandas" library in python and is tabulated with user IDs and screen names as columns. An additional column is present to match followers of the same tweet author from the original search query.

References:
- https://docs.tweepy.org/en/v4.0.0/api.html#tweepy.API
- https://www.geeksforgeeks.org/extracting-tweets-containing-a-particular-hashtag-using-python/
- https://phoenixnap.com/kb/windows-set-environment-variable
