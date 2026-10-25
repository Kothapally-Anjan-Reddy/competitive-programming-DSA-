# cook your dish here
T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    F=list(map(int,input().split()))
    C=list(map(int,input().split()))
    
    left=0
    right=0
    count=0
    current=0
    
    while left<len(F) and right<len(C):
        if current==0:
            if C[right]<F[left]:
                count+=1
                current=1
                right+=1
            else:
                left+=1
        else:
            if F[left]<C[right]:
                count+=1
                current=0
                left+=1
            else:right+=1
    
    if (current==0 and right<len(C)) or (current==1 and left<len(F)):
        count+=1
    
    print(count)
