import tweepy
import datetime
import json


def readConfig():
    json_file = open('config.json', 'r')
    json_obj = json.load(json_file)
    CK = json_obj['Consumer_key']
    CS = json_obj['Consumer_secret']
    AT = json_obj['Access_token']
    AS = json_obj['Access_secret']
    return [CK, CS, AT, AS]


def authTwitter():
    config = readConfig()
    auth = tweepy.OAuthHandler(config[0], config[1])
    auth.set_access_token(config[2], config[3])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return (api)


def getTwitterData(keyword, dfile):
    api = authTwitter()
    q = keyword

    tweets_data = []

    for tweet in tweepy.Cursor(api.search, q=q, include_entities=True, tweet_mode='extended').items():
        tweets_data.append(tweet.full_text + '\n')

    fname = r"'" + dfile + "'"
    fname = fname.replace("'", "")

    with open(fname, "w", encoding="utf-8") as f:
        f.writelines(tweets_data)


def main():
    print('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')

    print('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    getTwitterData(keyword, dfile)


if __name__ == "__main__":
    main()
