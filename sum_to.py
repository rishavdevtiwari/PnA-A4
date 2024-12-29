# 15. Sum : 1 to 10 (or any number) using for loop.
initial=int(input("Enter the initial value : "))
final=int(input("Enter the final value : "))
sum=0
for i in range(initial,final+1):
    sum+=i
print(f"SUM={sum}")