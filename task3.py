"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
* Write a script that will populate a list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your code here

def is_negative(number):

    if number <= 0:
        return True
    else:
        return False


# Ask user how many numbers should list have an convert to int
list_length = int(input("How many numbers should list have? "))


# Create empty list where numbers will be stored
list_of_numbers = []

# Ask user to input list_length numbers and append to list_of_numbers
for i in range(list_length):
    new_number = int(input("Enter integer number #" + str(i+1) + ": "))
    list_of_numbers.append(new_number)  # Add new number to the list

# Initialize total number of even and odd numbers
total_negative = total_non_negative = 0

for number in list_of_numbers:

    # Check if number is even
    if is_negative(number):
        total_negative += 1
    else:
        total_non_negative += 1


print("List of numbers: ", str(list_of_numbers))
print("Total non_negative numbers: ", total_non_negative)
print("Total negative: ", total_negative)