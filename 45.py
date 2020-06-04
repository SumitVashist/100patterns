
"""

Enter the number of rows: 5
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 


"""

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	print("  "*(n-i),end="")
	for j in range(1,i+1):
		print(chr(64+j),end=" ")
	for k in range(i-1,0,-1):
		print(chr(64+k),end=" ")
	print() 
