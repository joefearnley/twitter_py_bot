
import twitter.api

twitter_search = twitter.api.Twitter(domain="search.twitter.com")



s = twitter_search.search(q="hockey")

for tweet in s['results']:
    print tweet['text'] + "\n\n";

#print s['results'][0]['text']
