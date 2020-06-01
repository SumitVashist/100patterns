
"""
Enter the number of rows: 4
A A A A 
B B B B 
C C C C 
D D D D 


"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	for j in range(1,n+1):
		print(chr(i+64),end =" ")
	print() 
