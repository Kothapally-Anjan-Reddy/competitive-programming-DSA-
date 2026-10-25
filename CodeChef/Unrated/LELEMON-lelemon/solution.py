# cook your dish here
T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    P=list(map(int,input().split()))
    L=[]
    for i in range(N):
        V=list(map(int,input().split()))
        L.append(V[1:])
    
    res=0
    for i in P:
        if L[i]:
            num=max(L[i])
            res+=num
            L[i].remove(num)
    
    print(res)
