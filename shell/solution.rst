Objective
=========
To create a greet command which will print 'Hi' and a stock command which return the current share value.

The code can be run by :-

::
    
    $ python psh.py

or, if made executable

::
    
    $ ./psh.py

Explanation of the code
-----------------------

::
    
    from cmd2 import Cmd    #cmd2 module is imported for making command
    import requests         #requests module is imported for http requests
    import getpass
    
    __version__ = '0.1'
    
    class Application(Cmd):
            def __init__(self):    
                    Cmd.__init__(self)
    
            def do_hello(self, line):      # hello command is made which will print "Hello: line"
                    print "Hello:", line

            def do_sayit(self, line):      # sayit command is made which will print "python rocks"
                    print "Python rocks!"

            def do_greet(self, line):      # greet command is made which will print hi
                    x = getpass.getuser()
                    print "hi %s" % x
            def do_stock(self, line):      # stock command is made which will print sharevalue
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

Link
----
`click here <https://github.com/sheeshmohsin/repo01/blob/master/shell/psh.py>`_ for the link of actual code.
