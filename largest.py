# 19. Write a program to find the largest number in a list: [3, 7, 2, 8, 5].
sample=[3, 7, 2, 8, 5]
greatest=sample[0]
for num in sample:
    if num>greatest:
        greatest=num
print(f"The greatest number is {greatest}")