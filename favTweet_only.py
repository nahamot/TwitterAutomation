#coding:utf-8
import config
import tweepy
import time
# Accesss Token Secert

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

set_count = 100
word = "ここに検索するワードを書くよ"
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
        api.create_favorite(user_id) #ふぁぼする
        print(tweet)
        print("-----------------------------")
        print("をふぁぼしました(*‘ω‘ *)\n\n")
        print("-----------------------------")
        time.sleep(2)
    except:
        print(tweet)
        print("-----------------------------")
        print("はもうふぁぼしてます( ﾟДﾟ)\n\n")
        print("-----------------------------")
        time.sleep(2)
