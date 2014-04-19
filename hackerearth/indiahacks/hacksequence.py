T = int(raw_input(""))
for v in range(T):
	x = int(raw_input(""))
	array = [1,1]
	if x==1:
		y=1
	elif x==2:
		y=1
	else:
		for z in xrange(3,x+1):
			y=2014*array[1]+69*array[0]
			array.append(y)
			array.pop(0)
	output=array[1]%(1000000000+7)
	print output
