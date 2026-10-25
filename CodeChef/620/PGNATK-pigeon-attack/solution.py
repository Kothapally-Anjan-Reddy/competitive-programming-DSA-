# cook your dish here

T=int(input())

for _ in range(T):
    N,K=map(int,input().split())
    
    count=0 # work required
    i=0     # time elapsed
    while count<N:
        i+=1
        if i%K!=0:
            count+=1
    print(i)
