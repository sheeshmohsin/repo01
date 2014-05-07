N = int(raw_input(""))
S = raw_input()
for j in xrange(N):
	z,m=[],[]
	for x in S:
		z.append(x)
	for x in z:
		m.insert(0,x)
	if len(z)%2==0:
		l = len(z)/2
	else:
		l = len(z)/2 + 1
	w=""
	for y in xrange(l):
		w = w + z[y]
		if y!=l-1:
			w = w + m[y]
	S = w
print w