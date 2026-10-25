import heapq

T=int(input())

for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    
    max_heap=[]
    heapq.heapify(max_heap)
    removed=False
    total=0
    ans=True
    
    for i in A:
        total+=i
        if i<0:
            heapq.heappush(max_heap,i)
        if total<0 and removed==False:
            total-=heapq.heappop(max_heap)
            removed=True
        elif total<0 and removed==True:
            ans=False
            break
            
    if ans:
        print("YES")
    else:
        print("NO")
