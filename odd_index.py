# 14. Accept string from the user and display only those characters which are 
# present at an odd index.
str=input("Enter a string : ")
print("Characters at odd index are : ")
for i in range(len(str)):
    if i%2!=0:
        print(str[i],end="")