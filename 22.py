"""

Enter the number of rows: 8
H G F E D C B A 
H G F E D C B 
H G F E D C 
H G F E D 
H G F E 
H G F 
H G 
H 


"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	for j in range(1,n+2-i):
		print(chr(65+n-j),end=" ")
	print() 
