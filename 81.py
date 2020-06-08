"""

Enter the  number of rows:5
*****
*   *
*   *
*   *
*****


"""

rows=int(input("Enter the  number of rows:"))
for i in range(1, rows + 1): 
	if (i == 1 or i == rows): 
		for j in range(1, rows + 1):
			print("*", end = "") 
	else: 
		for j in range(1, rows + 1): 
			if (j == 1 or j == rows): 
				print("*", end = "") 
			else: 
				print(end = " ") 
	print() 
      
