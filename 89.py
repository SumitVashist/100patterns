"""

Enter a number : 10
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
*****         *****
*****         *****
*****         *****
*****         *****
*****         *****


"""
n = int(input("Enter a number : "))

for i in range(n): 
	for j in range(i + 1, n): 
		print(' ', end = '') 
	for j in range(0, 2 * i + 1): 
		print('*', end = '') 
	print() 
for i in range(n//2): 
	for j in range(n//2): 
		print('*', end = '') 
	for j in range(2 * n - 2 *(n//2) -1): 		
		print(' ', end = '') 
	for j in range(n//2): 
		print('*', end = '') 
	print() 



