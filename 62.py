"""

Enter a number:5
E 
D E 
C D E 
B C D E 
A B C D E 
B C D E 
C D E 
D E 
E 



"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
	for j in range(0,i):
		print(chr(65+num-i+j),end=" ")
	print()
for a in range(1,num+1):
	for k in range(1,num+1-a):
		print(chr(64+k+a),end=" ")
	print() 
