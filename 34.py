
"""

Enter the number of rows: 7
               * 
             * * * 
           * * * * * 
         * * * * * * * 
       * * * * * * * * * 
     * * * * * * * * * * * 
   * * * * * * * * * * * * * 



"""




n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
	print("  "*(n-i+1),"* "*(2*i-1)) 
