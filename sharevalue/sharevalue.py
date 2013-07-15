#!/usr/bin/env python

import urllib2
import sys

def share(symbol):
    try:
        b = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1')
        a = float(b.read())
        if a == 0.00:
            print "The Nasdaq code entered is wrong"
        else:
            print "The current sharevalue for the given NASDAQ symbol is %f" % (a)
    except:
        print "failed to open the finance.yahoo.com url"

if __name__ == '__main__':
        if len(sys.argv) !=2:
                print "Incorrect entry. Enter a NASDAQ symbol"
                sys.exit(1)
        else:
                share(sys.argv[1])
                sys.exit(1)
