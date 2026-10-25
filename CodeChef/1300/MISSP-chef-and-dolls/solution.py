# cook your dish here

T=int(input())

for i in range(0,T):
    N=int(input())
    # dici={}
    res=0
    for i in range(0,N):
        num=int(input())
        res^=num
    #     dici[num]=dici.get(num,0)+1
    
    # for key,value in dici.items():
    #     if value%2!=0:
    #         print(key)
    
    print(res)
