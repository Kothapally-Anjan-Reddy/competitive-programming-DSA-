# cook your dish here

T=int(input())

for _ in range(T):
    X1,Y1,X2,Y2=map(int,input().split())
    if X1==X2 and Y1==Y2:
        print(0)
    elif (X1-Y1)==(X2-Y2) or (X1+Y1)==(X2+Y2):
        print(1)
    elif (X1+Y1)%2!=(X2+Y2)%2:
        print(-1)
    else:
        print(2)
