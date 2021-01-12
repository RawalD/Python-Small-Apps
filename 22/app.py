"""
We'll say a number is cool if it's a multiple of 11 or if it is one more than a multiple of 11. 
Return true if the given non-negative number is cool. Use the % "modulus" operator 


    * <b>EXPECTATIONS:</b><br>
    isCool(22)   <b>---></b> true <br>
    isCool(23)    <b>---></b> true <br>
    isCool(24) <b>---></b> false <br>
    """


def is_cool(num):

    if num < 0:
        return 'Invalid input'

    if num % 11 == 0:
        return True
    elif (num % 11) == 1:
        return True
    else:
        return False


print(is_cool(22))
print(is_cool(23))
print(is_cool(24))
