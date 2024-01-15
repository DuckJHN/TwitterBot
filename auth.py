import tweepy
from keys import api_key,api_secret, access_token, access_token_secret,bearer_token


def get_twitter_conn_v1() -> tweepy.API:
    """Get twitter connection
    
    Returns:
        tweepy.API: Twitter API v1.1 Interface
    """
    auth = tweepy.OAuth1UserHandler(api_key, api_secret)
    auth.set_access_token(
        access_token, 
        access_token_secret
    )
    return tweepy.API(auth, wait_on_rate_limit= True)

def get_twitter_client() -> tweepy.Client:
    """Get twitter client

    Returns:
        tweepy.Client: Twitter API v2 Client
    """    
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    return client
    