# 5.Write a program to print the following using forloop
# a. first 10 odd numbers
c=0
for i in range(1,32):
    if c<10:
        if i % 2 != 0:
            print(f"{i}")
            c+=1
    else:
        break