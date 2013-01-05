from twitter import Twitter
from twitter import OAuth

# OAuth information
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# Supply the search terms. See the docs on the api search operators:
#    https://dev.twitter.com/docs/using-search
SEARCH_TERMS = "foo,bar"

def main():
    """Search the twitter timeline and befriend users."""
    t = authenticate()
    tweets = t.statuses.user_timeline()
    account_user_id = t.account.verify_credentials()['id']
    twitter_search = Twitter(domain="search.twitter.com")
    tweets = twitter_search.search(q=SEARCH_TERMS)['results']

    for tweet in tweets:
        from_user_id = tweet['from_user_id']
        is_following = (t.friendships.exists(user_id_a=account_user_id, user_id_b=from_user_id))
        if is_following == False:
            print "creating friendship between %s and %s " % (account_user_id, from_user_id)
            t.friendships.create(user_id=from_user_id)

    # print number of users following
    friends = t.friends.ids()["ids"]
    number_of_friends = len(friends)
    print "You are now following %s people on twitter." % number_of_friends

def authenticate():
    """Authenticate to Twitter API using OAuth and return Twitter object."""
    t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
    return t

def unfollow_all():
    """Utility to unfollow all users"""
    t = authenticate()
    friend_ids = t.friends.ids()["ids"]

    for id in friend_ids:
        t.friendships.destroy(user_id=id)

if __name__ == "__main__":
    main()
