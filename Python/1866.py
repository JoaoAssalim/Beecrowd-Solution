for x in range(int(input())):
	a = '1'
	for i in range(1, int(input())):
		if i % 2 == 0:
			a += '+1'
		else:
			a += '-1'
	print(eval(a))