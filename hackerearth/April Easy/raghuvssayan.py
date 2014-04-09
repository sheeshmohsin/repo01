t = int(raw_input())
for x in range(0,t):
	m = raw_input()
	m = m.split()
	a = int(m[0])
	b = int(m[1])
	n = int(m[2])
	dish = raw_input()
	dish = dish.split()
	raghu = 0
	sayan = 0
	for y in range(0, n):
		if raghu + int(dish[y]) < a:
			raghu = raghu + int(dish[y])
		if sayan + int(dish[y]) < b:
			sayan = sayan + int(dish[y])
	if raghu > sayan:
		print "Raghu Won"
	if sayan > raghu:
		print "Sayan Won"
	if raghu == sayan:
		print "Tie"