# min_max.py
# Conner Smith
# 2026-01-19
# Project 3b

print("How many integers would you like to enter?")
count = int(input())

print("Please enter", count, "integers.")

# Get the first number to start min and max
num = int(input())
minimum = num
maximum = num

# Loop through the rest of the numbers
for i in range(count - 1):
    num = int(input())
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("min:", minimum)
print("max:", maximum)
