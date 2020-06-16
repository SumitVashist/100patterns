"""

Enter number of rows : 5
5 4 3 2 1 1 2 3 4 5 

5 4 3 2     2 3 4 5 

5 4 3         3 4 5 

5 4             4 5 

5                 5 




"""


rows = int(input("Enter number of rows : "))
for i in range(0, rows+1):
    for j in range(rows , i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows+1):
        print(k, '', end='')
    print('\n')

