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
	print(" "*(num-i),end="")
	for j in range(0,i):
		print(num+j-i+1,end=" ")
	print()
for k in range(1,num):
	print(" "*k,end="")
	for l in range(1,num+1-k):
		print(l+k,end=" ")
	print()
