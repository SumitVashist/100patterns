"""


Enter the number of rows: 7
A B C D E F G 
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 



"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	for j in range(1,n+2-i):
		print(chr(64+j),end=" ")
	print() 
