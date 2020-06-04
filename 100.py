n=int(input("Enter a number:"))
for a in range(1,n+1,2):
	for i in range(1,n+1):
		print(" "*(2*n-i-a),end="")
		for j in range(1,i+a):
			print("*",end=" ")
		print()
for b in range(1,n+1):
	print(" "*(n-2),end="")
	print("* "*3) 
