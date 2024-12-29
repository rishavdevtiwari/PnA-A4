# 23. Write a program to print all numbers between 1 and 50 that are divisible by both 3 and 5.
for num in range(1,51):
    if num % 3 == 0 and num % 5 ==0:
        print(num, end=" ")