import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # Create a dictionary from sentiment score
    scores = {}
    for line in sent_file:
	term,score = line.split("\t")
	scores[term] = int(score)

    # Parse tweet file
    for line in tweet_file:
	sent_score = 0
	tweet = json.loads(line)
	if tweet.get('text'):
	    words = tweet['text'].encode('utf-8').split()
	    for word in words:
	        sent_score += scores.get(word,0)
	print sent_score

if __name__ == '__main__':
    main()
