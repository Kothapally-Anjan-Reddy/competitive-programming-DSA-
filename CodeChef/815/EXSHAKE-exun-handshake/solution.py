# cook your dish here
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    teams=0
    players=0
    for i in range(N):
        x=players+A[i]
        if (x*(x-1))/2 >M:
            break
        teams+=1
        players=x
    
    print(teams)
