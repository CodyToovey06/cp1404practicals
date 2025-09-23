for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A.
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# B.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C.
number_of_starts = int(input("Enter number of stars: "))
for i in range(0, number_of_starts):
    print("*", end='')

# D.
number_of_starts = int(input("Enter number of stars: "))
for i in range(0, number_of_starts + 1):
    print("*" * i)
