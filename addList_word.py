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

#ここまで恒例のヤツ

listword = "検索ワード" #検索ワード

for status in api.home_timeline(count=100): #自分のタイムラインのステータス取得（個別対応）
    userid = status.user.id #ツイートのユーザーid
    username = status.user.name #ツイートのユーザ名
    tweet = status.text #ツイートの内容
    print("--------------------------")
    print("名前:"+username)
    print(tweet)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    if listword in tweet or listword in username: #検索ワードがツイートかユーザー名に含まれていた場合
        api.add_list_member(user_id=userid, slug="list2", owner_screen_name="ユーザー名") #listにそのツイートのユーザ名を追加する
        print(listword+"リストに"+username+"を追加しました！")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    else:
        print(listword+"リストに"+username+"を追加しませんでした。")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
