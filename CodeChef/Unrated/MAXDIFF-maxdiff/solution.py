# cook your dish here

T=int(input())

for i in range(T):
    N,K=map(int,input().split())
    w=list(map(int,input().split()))
    
    w.sort()
    sum1=0
    sum2=0
    for i in range(0,K):
        sum1+=w[i]
        sum2+=w[N-i-1]
        
    sumi=sum(w)
    res1=sumi-sum1
    res2=sumi-sum2
    res=max(abs(res1-sum1),abs(res2-sum2))
    
    print(res)
