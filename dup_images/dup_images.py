import sys
import glob
import filecmp
import os
d=[]
e = [".jpg", ".gif", ".png", ".bmp", ".psd", ".thm", ".tif", ".pspimage"]
for x in sys.argv[1:]:
    if not os.path.exists(x):
	print "Invalid input"
    for z in e:
        for y in glob.glob(x+"/*"+z):
	    d.append(y)
l= len(d)
if l==0 or l==1:
    print "No. of images is 1 or less than 1 so can't compare"
else:
    for x in d[0:l-1]:
        for y in d[1:l]:
            if x!=y:
	        if filecmp.cmp(x,y,shallow=False) is True:
		    a, b = os.path.basename(x), os.path.basename(y)
	            print a, "and", b, "are similiar\n",
