# Write a program that prompts the user to input an integer and then outputs the number 
# with the digits reversed. For example, if the input is 12345, the output should be 54321.
num=input("Enter an integer with multiple digits : ")
for i in range(len(num)-1,-1,-1):
    print(f"{num[i]}",end=" ")