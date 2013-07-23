from cmd2 import Cmd
import requests
import getpass

__version__ = '0.1'

class Application(Cmd):
	def __init__(self):
		Cmd.__init__(self)

	def do_hello(self, line):
		print "Hello:", line

	def do_sayit(self, line):
		print "Python rocks!"

	def do_greet(self, line):
		x = getpass.getuser()
		print "hi %s" % x
	def do_stock(self, line):
		try:
			r = requests.get('http://download.finance.yahoo.com/d/quotes.csv?s='+line+'&f=l1')
			b = float(r.text)
			if b == 0.00:
				print "Invalid Nasdaq Code"
			else:
				print "%f" % (b)
		except:
			print "Connection Problem"

if __name__ == '__main__':
	app = Application()
	app.cmdloop()
