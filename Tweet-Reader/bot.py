import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'YPU6pIJXvS42DprZlTxYitb98'
consumer_secret = 'uRFkgko0MvZMzsVjld5NgIjYF1DHE8az8B97xz3pnZDdMgUaNm'
access_token = '1536381304241102849-kVRZ1oU90Iv4uu6POo4fmZqCWqVoCn'
access_token_secret = 'dbuU2pnQlM09Zi6VKlUHtp72eSNXnmN9B6uMGeAdhH0DX'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump', tweet_mode="extended").items():
    print(status.full_text)