# cook your dish here

n=int(input())

while(n>9):
    sum=0
    for i in str(n):
        sum+=int(i)
    
    n=sum
    
print(n)
