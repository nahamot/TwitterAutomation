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

try:
    api.update_status("リスト追加やっぱりあんまり自動でやらないほうがいいみたい。\n不審アクティビティ認識される。これから控えよう。")
    print("トゥイ―トしました(*‘ω‘ *)")
except:
    print("失敗した模様(´;ω;｀)")