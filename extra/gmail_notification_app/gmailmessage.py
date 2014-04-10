import urllib2
import subprocess
from bs4 import BeautifulSoup
 
FEED_URL = 'https://mail.google.com/mail/feed/atom'
 
def get_unread_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user='{user}@gmail.com'.format(user=user),
        passwd=passwd
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen(FEED_URL)
    soup = BeautifulSoup(feed.read())
    number = soup.fullcount.string
    unreadmessages = "You have %d unread mails in your gmail inbox" % int(number)
    sendmessage(unreadmessages)

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return
 
##########
 
if __name__ == "__main__":
    import getpass
 
    user = raw_input('Username: ')
    passwd = getpass.getpass('Password: ')
    print get_unread_msgs(user, passwd)
