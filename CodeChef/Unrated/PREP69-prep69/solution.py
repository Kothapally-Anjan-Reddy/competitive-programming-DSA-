# cook your dish here

T=int(input())

for i in range(T):
    N=int(input())
    A=[]
    for x in map(int,input().split()):
       if not A:
           A.append(x)
           
       elif A[-1]!=x:
           A.append(x)
           
    print(len(A))
    
    for x in A:
        print(x,end=" ")
        
    print()
