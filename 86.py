"""

Enter no of columns::7
            * 
          * * 
        * * * 
      * * * * 
    * * * * * 
  * * * * * * 
* * * * * * * 
  * * * * * * 
    * * * * * 
      * * * * 
        * * * 
          * * 
            * 




"""


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print()
    k = -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print()
 
n=int(input("Enter no of columns::")) 
pattern(n)
