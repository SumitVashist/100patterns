"""


Enter a number:5
*   *
*   *
*****
*   *
*   *
*****
*   *
*   *
*****
*   *
*   *
*****
*   *
*   *
*****
*   *
*   *

"""
N=int (input("Enter a number:" ))
for i in range(N + 1) : 
	print("*   *"); 
	print("*   *"); 

	if (i < N) : 
		print("*****"); 


