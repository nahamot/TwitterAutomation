#coding:utf-8
import config
import tweepy
# Accesss Token Secert

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

word = ["小説家になろう", "更新"]
my_id = "ユーザー名"
set_count = 100
results = api.search(q=word, count=set_count)

for result in results:
    username = result.user.name
    user_id = result.user.id
    tweet = result.text
    tweet_id = result.id
    print("ユーザー名："+username)
    print("ユーザーID："+str(user_id))
    print("-----------------------------")

    try:
        api.retweet(tweet_id) #RTする
        print(tweet)
        print("-----------------------------")
        print("をRTしました\n\n")
        print("-----------------------------")
    except:
        print(tweet)
        print("-----------------------------")
        print("はRTしてます\n\n")
        print("-----------------------------")
