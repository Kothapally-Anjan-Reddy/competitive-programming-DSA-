# cook your dish here
T=int(input())
for _ in range(T):
    N,S=map(int,input().split())
    total=0
    q=0
    while total<S:
        total+=4
        q+=1
    if total==S:
        print(q)
    else:
        while total>S and q<N:
            total-=1
            q+=1
        if q<=N and total==S:
            print(q)
        else:
            print(-1)
