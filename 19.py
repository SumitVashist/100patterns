
"""

Enter the number of rows: 7
7 7 7 7 7 7 7 
6 6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 


"""



n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	for j in range(1,n+2-i):
		print(n+1-i,end=" ")
	print() 
