T = int(raw_input(""))
a,i = 0,0
b,j = 0,0
for x in range(T):
	first = raw_input()
	second = raw_input()
	first = first.split()
	second = second.split()
	while a <= int(first[0]):
		a = a + int(second[i])
		if a > int(first[0]):
			a = a - int(second[i])
			break
		i = i + 1
		if i == len(second):
			break
		
	while b <= int(first[1]):
		b = b + int(second[j])
		if b > int(first[1]):
			b = b -int(second[j])
			break
		j = j + 1
		if j == len(second):
			break

	if a > b:
		print "Raghu Won"
	elif b > a:
		print "Sayan Won"
	else:
		print "Tie"
