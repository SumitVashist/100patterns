"""

Enter a number:5
A B C D E F G H I 
  A B C D E F G 
    A B C D E 
      A B C 
        A 


"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
	print("  "*(i-1),end="")
	for j in range(1,num+2-i):
		print(chr(64+j),end=" ")
	for k in range(2,num+2-i):
		print(chr(64+num+k-i),end=" ")
	print() 
