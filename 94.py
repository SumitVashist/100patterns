
"""

Enter the size of window :  7
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 


"""

n=int(input("Enter the size of window :  "))
if n % 2 != 0: 
	c = ( n // 2 ) + 1
	d = 0
else: 
	c = ( n // 2 ) + 1
	d = ( n // 2 ) 

for i in range( 1 , n + 1 ): 
	for j in range( 1 , n + 1 ): 
		if i == 1 or j == 1 or i == n or j == n: 
			print("*",end=" ") 
				
		else: 
			if i == c or j == c: 
				print("*",end=" ") 
			elif i == d or j == d: 
				print("*",end=" ") 
			else: 
				print(" ",end=" ") 
	print() 

