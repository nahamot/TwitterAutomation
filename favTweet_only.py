#coding:utf-8
import json, config
import tweepy
# Accesss Token Secert

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

word = "Amazonアフィリエイト"
set_count = 100
results = api.search(q=word, count=set_count)

for result in results:
    username = result.user._json['screen_name']
    user_id = result.id
    print("ユーザーID："+str(user_id))
    user = result.user.name
    print("ユーザー名："+user)
    tweet = result.text
    print("ユーザーのコメント："+tweet)

    try:
        api.create_favorite(user_id)
        print(user+"に「いいね」をしました\n\n")
    except:
        print(tweet+"はもういいねしてます\n\n")
