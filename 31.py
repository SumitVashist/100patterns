
"""
Enter the number of rows: 5
1 2 3 4 5 
 1 2 3 4 
  1 2 3 
   1 2 
    1 



"""

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	print(" "*(i-1),end="")
	for j in range(1,n+2-i):
		print(j,end=" ")
	print() 
