"""
Given 3 int arguments - a, b, c, return their sum. However, if one of the arguments 
is the same as any of the other ones, that number should not count towards the sum. 
So basically you only sum unique numbers, not duplicates
<br>
<br>

    * <b>EXPECTATIONS:</b><br>
    sumUnique(1, 2, 3)   <b>---></b> 6 <br>
    sumUnique(3, 2, 3)    <b>---></b> 2 <br>
    sumUnique(3, 3, 3) <b>---></b> 0 <br>
"""


def sum_unique(num, num2, num3):

    if num != num2 and num != num3:
        return num + num2 + num3
    else:
        return num2 + num3


print(sum_unique(1, 2, 3))
print(sum_unique(3, 2, 3))
print(sum_unique(3, 3, 3))
