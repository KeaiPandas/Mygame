i = 0
for i in range(101):
	if i % 7==0 or i % 10 == 7 or i // 10 == 7:
		continue
	print(i)

