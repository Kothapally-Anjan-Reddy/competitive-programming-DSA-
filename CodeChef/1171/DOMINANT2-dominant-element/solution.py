# cook your dish here

T=int(input())

for i in range(0,T):
    N=int(input())
    
    input_str=input()
    A={}
    for x in input_str.split():
        A[x]=A.get(x,0)+1
    
    A=list(sorted(A.items(),key=lambda x:x[1],reverse=True))
    
    first=A[0][1]
    second=0
    if len(A)>1:
        second=A[1][1]
    
    if first>second:
        print("YES")
    else:
        print("NO")
