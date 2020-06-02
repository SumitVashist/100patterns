"""

Enter the number of rows: 7
1 1 1 1 1 1 1 
2 2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 
5 5 5 
6 6 
7 




"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	for j in range(1,n+2-i):
		print(i,end=" ")
	print() 
