import math

T = int(raw_input(""))
for x in range(T):
	e = raw_input()
	e = e.split()
	factoria = 1
	question = 3 * int(e[0])
	factoria = math.factorial(question)

	result = (factoria/(6**int(e[0]))) % int(e[1])
	print result