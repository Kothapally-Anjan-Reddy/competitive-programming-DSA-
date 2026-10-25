# cook your dish here
T=int(input())

for i in range(T):
    N=int(input())
    if N>2:
        freq={}
        for x in map(int,input().split()):
            freq[x]=freq.get(x,0)+1
        
        max_freq = max(freq.values())
        
        x1=max_freq
        y1=N-x1+1
        
        if x1<2:
            print(-1)
        
        elif x1==N:
            print(0)
            
        else:
            print(y1)
            
    elif N==2:
        x,y=map(int,input().split())
        if x!=y:
            print(-1)
        else:
            print(0)
    else:
        x=int(input())
        print(0)
