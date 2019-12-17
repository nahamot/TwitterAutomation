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
follow_count = 0
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
    # Max100人までしか検索できないぽい。また、単語検索結果で検索結果出てきたアカウント数が上限となる。
    search_count = 100
    my_screen_name = "ユーザー名"

    followers_ids = api.followers_ids(my_screen_name)
    following_ids = api.friends_ids(my_screen_name)
    check_count = 0
    search_results = api.search(q=query, count=search_count)
    for result in search_results:
        # フォロー人数が特定人数以上になったらループ抜けて処理終了。
        if follow_count > 500:
            loop_out = True
            break
        user_id = result.user.id
        check_count += 1
        print("-----------------------------------------")
        print("[" + str(loop_count + 1) + "ループ目] 現状" + str(follow_count) + "人を新規フォロー。" + str(check_count) + "人目のアカウント(following_id:" + str(user_id) + ")をチェック開始！")
        # 検索結果のユーザーにすでにフォローされていたら、フォロー処理をせずにループを次に進める。
        if user_id in followers_ids:
            print("following_id:" + str(user_id) + ")からはすでにフォローされてたからスルー！")
            continue
        # 検索結果のユーザーをフォローしていたら、フォロー処理をせずにループを次に進める。
        if user_id in following_ids:
            print("following_id:" + str(user_id) + ")はすでにフォローしてたからスルー！")
            continue
        # 検索結果のユーザーのフォロワー数とフォロー数をカウント関数に入れる。
        user_follower_count = api.get_user(user_id).followers_count
        user_following_count = api.get_user(user_id).friends_count
        user_name = result.user.name
        screen_name = result.user.screen_name
        print("----------------------")
        # もしフォロー数100以上、フォロワー数100以下ならスルー
        if user_follower_count < 100:
            print(user_id, ":", user_name + "@" + screen_name, "はフォロワーが" + str(user_follower_count) + "人しかいないからフォローしませんでした")
        elif user_following_count < 100:
            print(user_id, ":", user_name + "@" + screen_name, "はフォローが" + str(user_following_count) + "人しかいないからフォローしませんでした")
        else:
            try:
                api.create_friendship(user_id)
                print(user_id, ":", user_name + "@" + screen_name, "はフォロワーが" + str(user_follower_count) + "人いて、未フォローだったのでフォローしました")
                follow_count += 1
            except:
                print(user_id, ":", user_name + "@" + screen_name, "はフォロー出来ませんでした。ブロックされてるか鍵垢かも？")

    print("----------------------------------")
    print(str(loop_count + 1) + "回目のループが終了しました")
    print("----------------------------------")
    # フォロー上限になったらループ抜ける
    if loop_out:
        break
    # アクセス連続しすぎるとやばいかもだから5分待つ（5分待つことで、153APIアクセス/5分 = 459APIアクセス/15分でAPIアクセス上限に引っかからないはず。）
    print("5分待ちます")
    time.sleep(300)
