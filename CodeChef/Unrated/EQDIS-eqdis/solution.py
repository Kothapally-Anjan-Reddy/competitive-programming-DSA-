# cook your dish here
T=int(input())

for i in range(T):
    N=int(input())
    A=set()
    for x in map(int,input().split()):
        if x not in A:
            A.add(x)
    
    u=len(A)
    print("YES") if (u%2==0 or N>u) else print("NO")
