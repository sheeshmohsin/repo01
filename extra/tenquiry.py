import urllib2
from bs4 import BeautifulSoup
e, name, fname = [], [], []
t=raw_input("Enter train no: ")
d=raw_input("Enter the date in dd format: ")
m=raw_input("Enter the month in mm format: ")
y=raw_input("Enter the year in yyyy format: ")
a= urllib2.urlopen('http://railenquiry.in/runningstatus/'+t+'/'+y+'-'+m+'-'+d+'/')
b=a.read()
soup = BeautifulSoup(b)
c=soup.find_all(class_="normal")
for z in c:
    e.append(z.string)
i, j = 0, 0
while j < len(e)/6:
    while i<6:
        name.append(e.pop(0))
        i+=1
    fname.append(name)
    name=[]
    j+=1
    i=0
print "\tStation\t",
print "\tSch.Arrival\t",
print "Sch.Departure\t",
print "\tStatus\t",
print "\tActual Arrival\t",
print "\tDelay"
for x in fname:
    for y in x:
        print "\t",y,
    print "\n"
