Objective of Assignment
=======================
The assignment was to write a program using python which prints the same output as in file /proc/mounts.

The python program written by me can be run using:-

::

    $ python mount.py
    
    # or, if it is executable, then using this command:-
    
    $./mount.py


My coded file is at this `link <https://github.com/sheeshmohsin/repo01/blob/master/mount/mount.py>`_

Explanation of my code
----------------------

::

    fp = open("/proc/mounts")
    
    """
    This line open the file /proc/mounts
    """
    
    print fp.read()
    
    """
    This line read and print the file.
    """
    
    fp.close()
    
    """
    This line closes the opened file.
    """
