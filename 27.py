"""

Enter the number of rows: 7
       A 
      B B 
     C C C 
    D D D D 
   E E E E E 
  F F F F F F 
 G G G G G G G 

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	print(" "*(n-i),(chr(64+i)+" ")*i)
print() 
