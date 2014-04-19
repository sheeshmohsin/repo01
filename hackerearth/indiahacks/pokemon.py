N = int(raw_input(""))
e = raw_input()
e = e.split()
i,j,k,d=0,0,0,0
z=[]
for x in e:
	if d<k:
		d=k
	k=j
	i=0
	x=int(x)
	while x>=0:
		z.append(i)
		z[k]=i
		x=x-1
		i=i+1
		k=k+1
	j=j+1
if d<k:
	d=k
print d+1
