"""

Enter the number of rows: 7
7 6 5 4 3 2 1 
7 6 5 4 3 2 
7 6 5 4 3 
7 6 5 4 
7 6 5 
7 6 
7 


"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	for j in range(1,n+2-i):
		print(n+1-j,end=" ")
	print() 
