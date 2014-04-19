N = int(raw_input(""))
e = raw_input()
e = e.split()
if len(e)==N:
	k = int(e[0]) + 1
	e.pop(0)
	i,j=2,0
	for x in e:
		x = int(x)
		z = x + i
		i = i + 1
		if z > k:
			k = z
	print k+1
