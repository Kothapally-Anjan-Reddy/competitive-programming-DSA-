# cook your dish here
T=int(input())

for i in range(T):
    N=int(input())
    max_people=1
    min_people=float('inf')
    maxi=1
    mini=1
    A=list(map(int,input().split()))
    prev=A[0]
    for curr in A[1:]:
        if curr-prev<=2:
            maxi+=1
            mini+=1
        else:
            max_people=max(max_people,maxi)
            min_people=min(min_people,mini)
            maxi=1
            mini=1
        prev=curr
    
    max_people=max(max_people,maxi)
    min_people=min(min_people,mini)
    
    print(min_people,max_people)
