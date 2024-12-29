# 13. Accept string from the user and display only those characters which are 
# present at an even index.
str=input("Enter a string : ")
print("Characters at even index are : ")
for i in range(len(str)):
    if i%2==0:
        print(str[i],end="")
    