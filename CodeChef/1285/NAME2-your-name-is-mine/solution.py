# cook your dish here

T=int(input())

for i in range(T):
    x,y=map(str,input().split())
    
    if len(x)>len(y):
        temp=y
        y=x
        x=temp
    
    
    p1=0
    p2=0
    res=0
    
    for i in range(len(y)):
        if x[p1]==y[p2]:
            p1+=1
            p2+=1
        else:
            p2+=1
        
        if p1>=len(x):
            res=1
            break
        
    print("YES") if res==1 else print("NO")
