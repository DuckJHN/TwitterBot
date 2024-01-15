import tweepy
from keys import api_key, bearer_token, api_secret, access_token, access_token_secret
from auth import get_twitter_conn_v1, get_twitter_client


client = get_twitter_client()
api = get_twitter_conn_v1()

def upload_media_and_get_media_id(filename):
    media = api.media_upload(filename=filename)
    return media.media_id_string

id = upload_media_and_get_media_id(filename="./images/nft1.png")
print(id)
client.create_tweet(text="Xin chao image", media_ids=[id])
print("Sucessfully uploaded")