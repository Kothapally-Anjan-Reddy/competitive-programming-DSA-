# cook your dish here
T=int(input())

for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    left=0
    right=N-1
    count=0
    
    while left<right:
        if A[left]==A[right]:
            left+=1
            right-=1
        elif A[left]<A[right]:
            diff=A[right]-A[left]
            A[right]=A[left]
            A.insert(right,diff)
            count+=1
            left+=1
        else:
            diff=A[left]-A[right]
            A[left]=A[right]
            A.insert(left+1,diff)
            count+=1
            left+=1
            
    print(count)
