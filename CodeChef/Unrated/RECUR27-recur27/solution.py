# cook your dish here

a,b=map(int,input().split())

def gcd(a,b):
    if a==1 or b==1:
        return 1
        
    elif a==0 or b==0:
        return max(a,b)
    else:
        res=gcd(b, a%b)
        return res
        
res=gcd(a,b)

print(res)
