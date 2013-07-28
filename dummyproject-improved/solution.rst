Objective
=========
To make a package which we can install in our system and to add dependencies in the setup.py project and add facebook posting commands.

Download
--------
`click here <https://testpypi.python.org/packages/source/s/shell/shell-1.7.tar.gz#md5=f451913304dd2e6777f0798eddd6ec16>`_ to download the package

How to Install
--------------
Extract the tar.gz file and change to the extracted directory from terminal and then type python setup.py install

Output
------
    This script is meant to run in virtualenv. The dependencies required to run it is automatically installed during installation. when we type fblogin command, a browser windows opens and asks for permission into your facebook account,after you give permission, you can post through command fbpost and can post photo through fbpicpost.

::
    
    (virt2)[sheesh@Sheesh shell-0.2]$ shell
    (Cmd) stock GOOG
    902.900000
    (Cmd) stock FB
    26.510000
    (Cmd) greet
    hi sheesh
    (Cmd) fblogin
    localhost.localdomain - - [28/Jul/2013 13:35:32] "GET / HTTP/1.1" 200 -
    localhost.localdomain - - [28/Jul/2013 13:35:32] "GET /?      access_token=CAACjeiZB6FgIBAEaW6oeLcV6kKz1xomlBUXMJJZCcMFGxq3YZBwKZCmH4NNynb0V0E
    ZBvslJISBqibFuJbZBMvv3n7h4ZAXvrSXlzh9PZCWh3ygEOX4krS1LbH8djCO0CMOlDBZAZAGERCQcghu7g0oMgLv3AaxaysBcaHzYglM0u06QZDZD&expires_in=6919         HTTP/
    1.1" 200 -
    (Cmd) fbpicpost images.jpg
    (Cmd) fbpost hi! what's up?



