"""

Enter a value : 5
\***/
*\*/*
**/**
*/*\*
/***\


"""


def printPattern(i,j, n): 
	if (j >= n) : 
		return 0
	if (i >= n): 
		return 1
	if (j == i or j == n - 1 - i): 
		if (i == n - 1 - j): 
			print("/",end="") 
		else: 
			print("\\",end="") 
	else: 
		print("*",end="") 
	if (printPattern(i, j + 1, n) 
		== 1): 
		return 1

	print() 
	return printPattern(i + 1, 0, n) 

if __name__ == "__main__": 
	N = int (input("Enter a value : "))
	printPattern(0, 0, N) 

