import urllib2
import subprocess
from bs4 import BeautifulSoup
import time
import ConfigParser

FEED_URL = 'https://mail.google.com/mail/feed/atom'

Config = ConfigParser.ConfigParser()
Config.read("config.ini")


def ConfigSectionMap(section):
    values = {}
    options = Config.options(section)
    for option in options:
        try:
            values[option] = Config.get(section, option)
            if values[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            values[option] = None
    return values


def internet_on():
    try:
        response = urllib2.urlopen('http://www.google.com')
        return True
    except:
    	return False


class Gmailnotification:

	def __init__(self, user, passwd):
		self.getnumberofmessage(user, passwd)

	def getnumberofmessage(self, user, passwd):
		auth_handler = urllib2.HTTPBasicAuthHandler()
		auth_handler.add_password(
			realm = 'New mail feed',
			uri = 'https://mail.google.com',
			user = '{user}@gmail.com'.format(user=user),
			passwd = passwd
		)
		opener = urllib2.build_opener(auth_handler)
		urllib2.install_opener(opener)
		feed = urllib2.urlopen(FEED_URL)
		soup = BeautifulSoup(feed.read())
		number = soup.fullcount.string
		number = int(number)
		unreadmessages = "You have %d unread mails in your gmail inbox" % int(number)
		self.sendmessage(unreadmessages, number)

	def sendmessage(self, message, number):
		nomessage = "No unread mails in your gmail inbox"
		self.previousnumber = 0
		if number == self.previousnumber:
			if number == 0:
				subprocess.Popen(['notify-send', nomessage])
				previousnumber = number
			else:
				return number
		else:
			subprocess.Popen(['notify-send', message])
			previousnumber = number


if __name__ == "__main__":
	previousnumber = 0
	while True:
		if internet_on():
			user = ConfigSectionMap("SectionOne")['username']
			passwd = ConfigSectionMap("SectionOne")['password']
			d = Gmailnotification(user, passwd)
			time.sleep(300)
		else:
			time.sleep(30)
