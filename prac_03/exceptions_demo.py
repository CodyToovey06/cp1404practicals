"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When an unexpected value is used - string or float instead of integer.
2. When will a ZeroDivisionError occur?
When a number is divided by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Use a while loop to get valid input from user
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while numerator == 0 or denominator == 0:
        if numerator == 0:
            print("Numerator cannot be 0, try again")
            numerator = int(input("Enter the numerator: "))
        else:
            print("Denominator cannot be 0, try again")
            denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
