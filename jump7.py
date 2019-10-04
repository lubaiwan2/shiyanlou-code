a=1
while a<= 100:
	if a % 7 == 0 or a % 10 == 7:
		a += 1
		continue
	elif a // 10 == 7:
		a += 1
		continue	
	else:
		print(a)
		a += 1
	
