# cook your dish here

T=int(input())

for i in range(T):
    n=int(input())
    
    input_str=input()
    li=[]
    for x in input_str.split():
        if int(x) not in li:
            li.append(int(x))
    print(len(li))
