# factors.py
# Conner Smith
# 2026-01-19
# Project 3b

num = int(input("Please enter a positive integer: "))

print("The factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
