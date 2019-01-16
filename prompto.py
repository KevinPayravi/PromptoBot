import tweepy, time, sys
import Image
import random

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

quotes = ["This place sure is romantic.", "Looks a lotta sketchy to me.", "Got it!", "Any chance of sleeping in a nice room tonight?", "I've decided I wanna become a professional photographer.", "Decent lighting, scenic background...yep, this is the spot!", 'Say, "Fuzzy pickles!"', "I wanna express my love in film.", "When we hang out, it's so much fun!", "You mad, bro?", "Oh, I love the lighting.", "You don't get that in every demon infested dungeon.", "This city at night is so...romantic.", "When I get the chance, I'm off hiking and taking pictures!", "I'm an avid photog."]

fileRead = open("/usr/bin/prompto/log.txt", "rb")
lines = fileRead.readlines()
lastRow = lines[-1]
fileRead.close
lastRow = lastRow.replace("\n", "")
newFile = int(lastRow) + 1

try:
	background = Image.open("/usr/bin/prompto/backgrounds/" + str(newFile) + ".jpg")
except:
	background = Image.open("/usr/bin/prompto/backgrounds/1.jpg")
	newFile = int(1)

foreground = Image.open("/usr/bin/prompto/prompto.png")
foreground.thumbnail(background.size)

fileWrite = open("/usr/bin/prompto/log.txt", "a")
fileWrite.write("\n" + str(newFile))
fileWrite.close

width, height = background.size
background.paste(foreground, (80, int(int(height) * .25)), foreground)
background.save("/usr/bin/prompto/backgrounds/" + str(newFile) + "new.jpg")

api.update_with_media("/usr/bin/prompto/backgrounds/" + str(newFile) + "new.jpg", random.choice(quotes))
