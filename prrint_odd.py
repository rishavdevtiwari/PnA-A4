# 17. Write a Python program to print the odd numbers from a given list. 
# Sample List : [12,13,14,15,16,17,18,19]
sample=[12,13,14,15,16,17,18,19]
for i in sample:
    if i%2!=0:
        print(i,end=" ")