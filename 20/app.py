"""
The birds in Florida like to sing during favorable temperatures. 
In particular, they sing if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. 
Given an int temperature and a boolean isSummer, 
return true if the birds are singing and false otherwise. <br>
<br>

    * <b>EXPECTATIONS:</b><br>
    birdsSinging(70, false)   <b>---></b> true <br>
    birdsSinging(95, false)    <b>---></b> false <br>
    birdsSinging(95, true) <b>---></b> true <br>
"""


def birds_singing(temp, summer_season):

    sing_temps = 0

    if summer_season == True:
        sing_temps = 100
    else:
        sing_temps = 90

    if temp >= 60 and temp <= sing_temps:
        return True
    else:
        return False


print(birds_singing(70, False))
print(birds_singing(95, False))
print(birds_singing(95, True))
