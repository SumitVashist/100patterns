"""

Enter a number:5
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 


"""

num=int(input("Enter a number:"))
for i in range(1,num+1):
	for j in range(1,i+1):
		print(num-i+j,end=" ")
	print()
for a in range(1,num+1):
	for k in range(1,num-a+1):
		print(k+a,end=" ")
	print() 
