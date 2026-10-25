
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    res=1
    
    if N<13 or A[0]!=1:
        res=0
    
    if res:
        for x in A:
            if x>7 or x<1:
                res=0
        
    if res:
        left=0
        right=N-1
        while left<right:
            if A[left]!=A[right]:
                res=0
                break
            left+=1
            right-=1
    
    if res:
        expected=1    
        for p in range(1,N//2 + 1):
            if A[p]==expected:
                continue
            elif A[p]==expected+1:
                expected+=1
            else:
                res=0
                break
        
        if expected!=7:
            res=0
        
    if res==0:
        print("no")
    else:
        print("yes")
