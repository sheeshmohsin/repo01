Objective
=========
Write a python script to print the latest share value of a company whose NASDAQ symbol would be given as command line argument.

This script can be run by these commands:

::
    
    $ python sharevalue.py [Nasdaq Symbol]

or, if made executable,

::
    
    $ ./sharevalue.py [Nasdaq Symbol]

Explanation of the code
-----------------------

::
    
    #!/usr/bin/env python

    import urllib2     # the module is imported for opening url
    import sys         # sys module is imported for command line arguments

    def share(symbol):     # The function is defined for opening and reading the url, and for printing sharevalue
        try:               # Used for handle exception and error may be due to problems like url not opening
            b = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1')     # opens the url
            a = float(b.read())                   # Reads the url
            if a == 0.00: # if any wrong symbol is entered then it print the sharevalue zero , which is not right, so removing it by if-else statement
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


~                                   
