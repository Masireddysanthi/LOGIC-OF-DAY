n=int(input("enter n value"))
sum=0
while(n>0):
    remainder = n % 10
    sum = sum + remainder
    n =n//10
print(sum)


