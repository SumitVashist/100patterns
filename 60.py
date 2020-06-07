"""

Enter a number:5
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
5 4 3 2 1 0 
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 


"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
	for j in range(0,i):
		print(num-j,end=" ")
	print()
for a in range(0,num+1):
	for k in range(0,num+1-a):
		print(num-k,end=" ")
	print() 
