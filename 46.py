"""

Enter the number of rows: 10
                  0 
                1 0 1 
              2 1 0 1 2 
            3 2 1 0 1 2 3 
          4 3 2 1 0 1 2 3 4 
        5 4 3 2 1 0 1 2 3 4 5 
      6 5 4 3 2 1 0 1 2 3 4 5 6 
    7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 
  8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 
9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 


"""





n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	print("  "*(n-i),end="")
	for j in range(1,i):
		print(i-j,end=" ")
	for k in range(0,i):
		print(k,end=" ")
	print()
