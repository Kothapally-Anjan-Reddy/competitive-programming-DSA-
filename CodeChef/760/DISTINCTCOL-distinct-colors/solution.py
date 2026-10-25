# cook your dish here

T=int(input())
for i in range(T):
    N=int(input())
    ele=0
    for s in map(int,input().split()):
        ele=max(ele,s)
        
    print(ele)
