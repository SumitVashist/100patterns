"""

Enter the number of rows: 7
 * * * * * * * 
  * * * * * * 
   * * * * * 
    * * * * 
     * * * 
      * * 
       * 

"""

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	print(" "*(i-1),"* "*(n+1-i))
