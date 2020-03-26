import config
import tweepy
import time

# TwitterAPIの認証データを取得して認証
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

# 特定の単語でつぶやいているユーザーを5人検索して、フォローされておらず、フォロワーが200人以上いればフォロー。
fav_count = 0
loop_out = False
for loop_count in range(7):
    print("----------------------------------")
    print(str(loop_count + 1) + "回目のループ開始！")
    print("----------------------------------")
    if loop_count == 0:
        query = "#おはようvtuber"
    elif loop_count == 1:
        query = "#おやすみvtuber"
    elif loop_count == 2:
        query = "ボイチェン"
    elif loop_count == 3:
        query = "ナナチ"
    elif loop_count == 4:
        query = "つくし卿"
    elif loop_count == 5:
        query = "メイアビ"
    elif loop_count == 6:
        query = "ロドス"
    elif loop_count == 7:
        query = "アークナイツ"
    # Max100人までしか検索できないぽい。また、単語検索結果で検索結果出てきたアカウント数が上限となる。
    search_count = 70
    results = api.search(q=query, count=search_count)
    for result in results:
        #  いいねした人数が特定人数以上になったらループ抜けて処理終了。
        if fav_count > 400:
            loop_out = True
            break
        user_id = result.user.id
        user_name = result.user.name
        tweet = result.text
        tweet_id = result.id

        print("ユーザー名：" + user_name)
        print("ユーザーID：" + str(user_id))
        print("-----------------------------")

        try:
            api.create_favorite(tweet_id)  # ファボする
            print(tweet)
            print("-----------------------------")
            print("をファボしました( ੭˙꒳ ˙)੭\n\n")
            print("-----------------------------")
            fav_count += 1
            time.sleep(3)
        except:
            print(tweet)
            print("-----------------------------")
            print("はファボしてます('ω')\n\n")
            print("-----------------------------")

    print("----------------------------------")
    print(str(loop_count + 1) + "回目のループが終了しました")
    print("----------------------------------")
    # ファボ上限になったらループ抜ける
    if loop_out:
        break
    # アクセス連続しすぎるとやばいかもだから5分待つ（5分待つことで、153APIアクセス/5分 = 459APIアクセス/15分でAPIアクセス上限に引っかからないはず。）
    print("5分待ちます")
    time.sleep(300)
