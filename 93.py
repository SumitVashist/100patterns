
"""

Enter number of rows : 7
* * * * * * * * * * * * * * 

* * * * * *     * * * * * * 

* * * * *         * * * * * 

* * * *             * * * * 

* * *                 * * * 

* *                     * * 

*                         * 

                            




"""


rows = int(input("Enter number of rows : "))
for i in range(0, rows+1):
    for j in range(rows , i, -1):
        print('*', '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows+1):
        print('*', '', end='')
    print('\n')

