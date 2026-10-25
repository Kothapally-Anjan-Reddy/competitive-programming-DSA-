# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    s=[]
    n=[]
    plus=0
    minus=0
    for c in input():
        if c.isdigit():
            n.append(c)
        else:
            if c=='+': 
                plus+=1
            else:
                minus+=1
            s.append(c)
    
    n=sorted(n,reverse=True)
    
    big_num=""
    for i in range(len(n)-len(s)):
        big_num+=n[i]
        
    result=str(big_num)
    i+=1
    
    while plus>0:
        result+="+"+n[i]
        i+=1
        plus-=1
    
    while minus>0:
        result+="-"+n[i]
        i+=1
        minus-=1
        
    print(result)
