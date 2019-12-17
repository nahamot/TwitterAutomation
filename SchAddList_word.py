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

add_count = 0
loop_out = False

for loop_count in range(7):
    print("----------------------------------")
    print(str(loop_count + 1) + "回目のループ開始！")
    print("----------------------------------")
    if loop_count == 0:
        query = "検索ワード１" # １ループ目の検索ワード
    elif loop_count == 1:
        query = "検索ワード２"
    elif loop_count == 2:
        query = ["検索ワード３","検索ワード４"]
    elif loop_count == 3:
        query = "検索ワード５"
    elif loop_count == 4:
        query = "検索ワード６"
    elif loop_count == 5:
        query = "検索ワード７"
    elif loop_count == 6:
        query = "検索ワード８"
    elif loop_count == 7:
        query = "検索ワード９"

    search_count = 30 # 検索数（上限１００）
    search_results = api.search(q=query, count=search_count)

    for result in search_results:
        # リスト追加人数が300人以上になったらループ抜けて処理終了。
        if add_count > 150:
            loop_out = True
            break
        userid = result.user.id # ツイート主のid（数字）
        username = result.user.name # ツイート主の名前
        tweet = result.text # ツイート内容
        tweetid = result.id # ツイートのid（数字）
        print("--------------------------------------------------")
        print("名前:"+username)
        print("ツイート:")
        print(tweet)
        print("--------------------------------------------------")
        try:
            api.add_list_member(user_id=userid, slug="list3", owner_screen_name="ユーザー名") #listにそのツイートのユーザ名を追加する
            print(username+"をリストに追加させていただきました。")
            add_count += 1
        except:
            print(username+"をリストに追加できませんでしたぁ！　ご主人様ァ(´;ω;｀)")

        try:
            api.create_friendship(userid)
            print(username+"をフォローしました。")
        except:
            print(username+"をフォローできませんでしたぁ！　ご主人様ァ(´;ω;｀)")

        print("-----------------------------------------")
        print("[" + str(loop_count + 1) + "ループ目] 現状" + str(add_count) + "人をリスト追加しました！")

    print("----------------------------------")
    print(str(loop_count + 1) + "回目のループが終了しました")
    print("----------------------------------")
    # フォロー上限になったらループ抜ける
    if loop_out:
        break
    # アクセス連続しすぎるとやばいかもだからループが終わったら5分待つ（5分待つことで、153APIアクセス/5分 = 459APIアクセス/15分でAPIアクセス上限に引っかからないはず。）
    print("5分待ちます")
    time.sleep(300)
