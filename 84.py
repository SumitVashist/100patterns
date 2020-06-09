num= int (input("Enter your number"))

for i in range (num):
	for j in range(num):
		if i==j or j+i==num-1:
			print("*",end=' ')
		else:
			print(" ",end=' ')
	print()
