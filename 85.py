"""

Enter your number: 5
X O O O X 
O X O X O 
O O X O O 
O X O X O 
X O O O X 


"""

num= int (input("Enter your number: "))

for i in range (num):
	for j in range(num):
		if i==j or j+i==num-1:
			print("X",end=' ')
		else:
			print("O",end=' ')
	print()
