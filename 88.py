"""

Enter your row : 14
**************
******__******
*****____*****
****______****
***________***
**__________**
*____________*



"""


rows = int(input("Enter your row : "))
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2

