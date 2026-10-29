# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    S=input()
    alarm=0
    coverage=N
    for i in range(N-1,-1,-1):
        if S[i]=='1' and coverage>i:
            alarm+=1
            coverage=max(0,i-K)
    print(alarm)
