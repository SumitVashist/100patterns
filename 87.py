"""

Enter a number:5
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 



"""
num=int(input("Enter a number:"))
for i in range(1,num):
	print(" "*(i-1),end="")
	for j in range(1,num+2-i):
		print("*",end=" ")
	print() 

for i in range(1,num+1):
	print(" "*(num-i),end="")
	for j in range(1,i+1):
		print("*",end=" ") 
	print()
