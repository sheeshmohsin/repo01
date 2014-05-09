import itertools
T = int(raw_input(""))
y = 6
for x in xrange(T):
	s = raw_input()
	s = s.split()
	N = int(s[0])
	M = int(s[1])
	a = list(itertools.product([2,4,6],repeat=N))

