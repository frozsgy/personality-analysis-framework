import twitter.tweet

def up(text):
	return text.upper()

t = twitter.tweet.Tweet(12, 12456465, "hello from the other side", True)

print(list(t.get_csv()))
t.map_tweet(up)

print(list(t.map_tweet(up).get_csv()))