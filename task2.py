"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

def pro_digits(number):

    # Chek if passed number is integer
    if not isinstance(number, int):
        return -1


    digit_pro = 1




    while number > 1:
        digit = number % 10
        number = number // 10
        digit_pro *= digit

    return digit_pro


def main():

    int_number = 1234
    digit_pro = pro_digits(int_number)
    print("Pro of digits for given numbers is: ", digit_pro)

main()












