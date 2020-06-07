"""


Enter a number:5
    5 
   5 4 
  5 4 3 
 5 4 3 2 
5 4 3 2 1 
 5 4 3 2 
  5 4 3 
   5 4 
    5 



"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
	print(" "*(num-i),end="")
	for j in range(1,i+1): 
		print(num-j+1,end=" ")
	print()
for k in range(1,num):
	print(" "*k,end="")
	for l in range(1,num+1-k):
		print(num-l+1,end=" ")
	print() 
