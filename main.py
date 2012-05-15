
import twitter
import oauth

# OAuth information
TOKEN = ""
TOKEN_KEY = ""
CONSUMER_SECRET = ""
CONSUMER_KEY = ""

# Search terms, seperated by comma
SEARCH_TERMS = "foo,bar"

def main():
    auth = OAuth(TOKEN, TOKEN_KEY, SECRET, SECRET_KEY)
    t = Twitter(auth)

    # TODO: parse term string and use OR operator

    twitter_search = Twitter(domain="search.twitter.com")
    tweets = twitter_search.search(q=SEARCH_TERMS)['results']

    for tweet in tweets:
        print tweet['text'] + "\n"
        # check to see if are friends with the user
        # if so, ignore,
        # if not, follow

if __name__ == "__main__":
    main()
