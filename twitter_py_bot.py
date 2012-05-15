
import twitter

SEARCH_TERMS = ""

def main():
    t = twitter.Twitter(domain="search.twitter.com")
    tweets = t.search(q="hockey")['results']

    for tweet in tweets:
        print tweet['text'] + "\n"


if __name__ == "__main__":
    main()
