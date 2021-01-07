"""
    Given a string of odd length, return the middle 3 characters from the string, 
    so the string "Monitor" yields <b>"nit". 
    If the string length is less than 3, return the string as is.

    EXPECTATIONS:
    middleThree("bunny")  "unn"
    middleThree("peter")  "ete"
    middleThree("Jamaica") "mai"
    """


def find_middle(usr_str):
    # Take the user string lenght and subtract 2 from it
    # Use integer division after the above result
    # This is our start range
    # Go upuntil the same method but replace -1 with +2
    """
    Length of our string: BUNNY = 5
    5 - 2 = 3
    3 // 2 = 1
    Start = U

    Length of our string: BUNNY = 5
    5 + 3 = 8
    8 // 2 = 4
    Emd = Y

    Start at U...N...N STOP BEFORE Y
    Middle three found
    """
    return usr_str[(len(usr_str) - 2) // 2: (len(usr_str) + 3) // 2]


user_input = input("Please Enter The Word To Find Its Middle\n")

print(find_middle(user_input))
