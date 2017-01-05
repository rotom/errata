from TwitterSearch import *
from pprint import *
import ParentTweetFetcher as ptf

replies = []
replies_with_parents = []

infile = 'C:/Users/rotom/Desktop/noyeah.txt'
outfile = 'C:/Users/rotom/Desktop/noyeahnew.txt'

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def get_parent(tweet):
        
    parent_user = tweet['in_reply_to_screen_name']
    parent_id = tweet['in_reply_to_status_id']
    tuo = TwitterUserOrder(parent_user)
    
    try:
        for parent in ts.search_tweets_iterable(tuo):
            if parent['id'] == parent_id:
                print 'PARENT: %s \nREPLY: %s' % (parent['text'], tweet['text'])
                replies_with_parents.append((tweet, parent))
        #print parent_user, parent_id, e


if __name__ == '__main__':

    with open(infile, 'w') as f:
        
    
        try:
            tso = TwitterSearchOrder()
            tso.set_keywords(["no yeah"]) #each keyword is a case/punctuation-insensitive substring
            tso.set_language('en') #filter non-English-tagged tweets
            tso.set_include_entities(False)

            # initiate TwitterSearch with appropriate tokens
            ts = TwitterSearch(consumer_key, consumer_secret, access_token, access_token_secret)
            #seed replies
            count = 0
            for tweet in ts.search_tweets_iterable(tso):

                tweet_minus_hashes = filter(lambda x:x[0]!='@', tweet['text'].split())
                
                if count >= 500:
                    print 'done'
                    break
                if tweet['in_reply_to_status_id'] != None and tweet['id'] not in replies:
                    f.write(str(tweet)+'\n\n')
                    print tweet['text']
                    replies.append(tweet['id'])
                    count += 1
                    print count

        except TwitterSearchException as e: #take care of all those ugly errors if there are some
            print(e)

    ptf = ptf.ParentTweetFetcher(infile, outfile)
    ptf.get_tweets_and_parents() 
    
