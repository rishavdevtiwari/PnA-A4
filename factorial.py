# 8. Write a program to print the factorial of a number accepted from user.
fact=1
num = int(input("Enter a number: "))
for i in range(1, num + 1):
        fact *= i   
print(f"Factorial  {num} is: {fact}")