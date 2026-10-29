# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    S=input()
    A=0
    B=0
    res=0
    for s in S:
        if s=='A':
            B=0
            A+=1
            if A==3:
                res+=1
                A=0
        else:
            B+=1
            A=0
            if B==3:
                res+=1
                B=0
    print(res)
