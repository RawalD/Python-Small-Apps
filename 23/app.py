"""
Given an int n, return the string form of the number followed by "!". 
So if the int is for example 13 this method should return "13!". 
However the catch is that if the number is divisible by 3 the method should return "Fizz!" 
instead of the number, and if the number is divisible by 5 it should return "Buzz!", 
and if divisible by both 3 and 5, use "FizzBuzz!". You’ll need to use the % "mod" 
for computing the remainder after division, so 23 % 10 yields 3. 

<br>
<br>

    * <b>EXPECTATIONS:</b><br>
    fizzyWizzy(1)   <b>---></b> "1!" <br>
    fizzyWizzy(2)    <b>---></b> "2!" <br>
    fizzyWizzy(3) <b>---></b> "Fizz!" <br>
"""


def fizzy_wizzy(num):

    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return f"{num}!"


print(fizzy_wizzy(1))
print(fizzy_wizzy(2))
print(fizzy_wizzy(3))
