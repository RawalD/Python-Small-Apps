"""
    * Given three ints, a b c, return true if it is possible to add two of 
    * the ints to get the third. There should only be a single line of code in the method body.<br>
    * <br> 
    *
    * <b>EXPECTATIONS:</b><br>
    twoSumOne(1, 2, 3)   <b>---></b> true <br>
    twoSumOne(3, 1, 2)    <b>---></b> true <br>
    twoSumOne(3, 2, 2) <b>---></b> false <br>
    """


def two_sum_one(num, num2, num3):
    if (num + num2) == num3:
        return True


print(two_sum_one(1, 2, 3))
