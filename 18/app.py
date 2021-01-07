
"""
    * You are driving a little too fast, and a police officer stops you. 
    * Write code to compute the fine you would have to pay. 
    * If your speed is 60 or less, the result is 0 since there is no fine. 
    * If speed is between 61 and 80 inclusive, the fine is 100 dollars. 
    * If speed is 81 or more, the result is 200. 
    * Unless it is a holiday -- on that day, your speed can be 5 higher in all cases. <br>
    * <br> 
    *
    * <b>EXPECTATIONS:</b><br>
    speedingFine(60, false)  <b>---></b> 0 <br>
    speedingFine (65, false)   <b>---></b> 100 <br>
    speedingFine (65, true) <b>---></b> 0 <br>
"""


def speeding_fine(speed, holiday):

    if holiday == "yes":

        if speed <= 60:
            return "No fine"

        elif speed >= 61 and speed <= 81:
            return "R100 fine"

        elif speed >= 81:
            return "R200 fine"

    else:

        if speed <= 65:
            return "No fine"

        elif speed >= 66 and speed <= 86:
            return "R100 fine"

        elif speed >= 86:
            return "R200 fine"


print("JMPD Ticketing System")

suspect_speed = int(
    input("Please enter the speed suspect was travelling at: "))
is_holiday_check = input("Please input if it is a holiday: ").lower()

print(speeding_fine(suspect_speed, is_holiday_check))
