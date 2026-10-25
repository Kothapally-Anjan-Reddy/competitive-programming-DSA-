# cook your dish here
T=int(input())

for _ in range(T):
    count=0
    N=int(input())
    A=set(map(int,input().split()))
    
    for x in map(int,input().split()):
        if x in A:
            count+=1
            
    print(count)
