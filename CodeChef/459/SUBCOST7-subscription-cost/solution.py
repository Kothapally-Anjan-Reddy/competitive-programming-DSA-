# cook your dish here

T=int(input())

for _ in range(T):
    N,X,Y=map(int,input().split())
    if N<=3:
        print(N*X)
    else:
        res=(N-3)*Y
        res=(3*X)+res
        print(res)
