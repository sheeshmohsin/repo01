def permutations(word):
	if len(word)<=1:
		return [word]
	perms=permutations(word[1:])
	char=word[0]
	result=[]
	for perm in perms:
		for i in range(len(perm)+1):
			result.append(perm[:i] + char + perm[i:])
	return result

testcase = int(raw_input(""))
for test in range(testcase):
	exactword=raw_input()
	sentence=raw_input()
	wordlist = permutations(exactword)
	for word in wordlist:
		check=word
		if check in sentence:
			d=2
			print "YES"
			break
		else:
			d=1
			continue
	if d==1:
		print "NO"
