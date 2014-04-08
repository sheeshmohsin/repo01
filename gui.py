#!/usr/bin/env python

import Tkinter
import urllib2
from Tkinter import *

class ShareValue:
	
	def __init__(self):
		self.top = Tk()
		self.top.wm_title("ShareValue Finder")
		self.top.geometry('500x200')
		self.cwd=StringVar(self.top)
		self.result = StringVar(self.top)
		self.dirfm = Frame(self.top)
		self.label = Tkinter.Label(self.dirfm,text='Enter NASDAQ Symbol',font='Helvetica -16 bold')
		self.label.pack()
		self.label = Label(self.dirfm,text="")
		self.label.pack()


		self.dirn = Entry(self.dirfm, width=50, textvariable=self.cwd)
		self.dirn.bind('<Return>', self.share)
		self.dirn.pack()
		self.result="Enter Symbol and press Enter Key"
		self.label1 = Label(self.dirfm,text="")
		self.label1.pack()
		self.label = Label(self.dirfm,text=self.result)
		self.label.pack()
		self.dirfm.pack(expand=1)

		self.frm = Frame(self.top)
		self.clear = Tkinter.Button(self.frm, text='Clear', command=self.clear, bg='red', fg='white')
		self.clear.pack(side=LEFT)
		self.quit = Tkinter.Button(self.frm, text='Exit', command=self.top.quit, bg='red', fg='white')
		self.quit.pack(side=LEFT)
		self.frm.pack()
	
	
	def share(self, ev=None):
		symbol = self.cwd.get()
		self.label.config(text="Please Wait ...")
		self.label.update()
		try:
			b = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1')
			a = float(b.read())
			if a == 0.00:
				result="The Nasdaq code entered is wrong"
				self.label.config(text=result)
				self.label.update()
			else:
				result="The current sharevalue for the given NASDAQ symbol is $%f" % (a)
				self.label.config(text=result)
				self.label.update()
		except:
			result="failed to open the finance.yahoo.com url"
			self.label.config(text=result)
			self.label.update()
	
	def clear(self, ev=None):
		self.dirn.delete(0, Tkinter.END)
		self.label.config(text="Enter Symbol and press Enter Key")
		self.label.update()
		
		
def main():
	mainloop()
	
if __name__ == '__main__':
	d = ShareValue()
	main()
