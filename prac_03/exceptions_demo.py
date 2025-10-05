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
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")