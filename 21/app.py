"""
	
	Given three ints, first, second, third, return true if second is greater than first, and third is 
	greater than second. However, with the exception that if the parameter "itsOk" is true, 
	second does not need to be greater than first but still better be less than third.
	<br>
	<br>

	 * <b>EXPECTATIONS:</b><br>
		isOrdered(1, 2, 4, false)   <b>---></b> true <br>
		isOrdered(1, 2, 1, false)    <b>---></b> false <br>
		isOrdered(1, 1, 2, true) <b>---></b> true <br>
	 
"""


def is_ordered(num, num2, num3, check_cond):

    if (num < num2 and num3 > num2 and check_cond == False):
        return True
    elif (num2 < num3 and check_cond == True):
        return True
    else:
        return False


print(is_ordered(1, 2, 4, False))
print(is_ordered(1, 2, 1, False))
print(is_ordered(1, 1, 2, True))
