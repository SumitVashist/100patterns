
"""

Enter the number of rows: 7
A B C D E F G 
 A B C D E F 
  A B C D E 
   A B C D 
    A B C 
     A B 



"""

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	print(" "*(i-1),end="")
	for j in range(65,66+n-i):
		print(chr(j),end=" ")
	print()
