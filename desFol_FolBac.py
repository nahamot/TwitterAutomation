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

user_id = "ユーザーid" #ここに自分のuseridを入れる
followers_id = api.followers_ids(user_id) #自分のアカウントのフォロワーをすべて取得する
following_id = api.friends_ids(user_id) #自分のアカウントのフォローをすべて取得する

time_count = 0
end_count = 0

for following in following_id: #自分がフォローしているユーザーだけ取得する
    if following not in followers_id: #自分のフォローしているユーザーで、フォロワーに属さないユーザーを取得する　
        user_follower_count = api.get_user(following).followers_count
        user_following_count = api.get_user(following).friends_count
        username = api.get_user(following).name
        if end_count > 80:
            print("80人リムーブしたので終了します。")
            break
        if time_count > 10:
            print("10カウントしたので5分待ちます")
            time.sleep(300)
            time_count = 0
        if user_following_count == 0:
            print("-------------------------------------")
            print("リムーブするユーザー名は",username,"です。")
            print("フォロー数は",user_following_count,"フォロワー数は",user_follower_count,"です。")
            print("-------------------------------------")
            api.destroy_friendship(following)
            time_count += 1
            end_count += 1
        if user_follower_count < 20*user_following_count:
            print("-------------------------------------")
            print("リムーブするユーザー名は",username,"です。")
            print("フォロー数は",user_following_count,"フォロワー数は",user_follower_count,"です。")
            print("-------------------------------------")
            api.destroy_friendship(following)
            time_count += 1
            end_count += 1
        else:
            print(username,"はリムーブしません")
            time_count += 1
