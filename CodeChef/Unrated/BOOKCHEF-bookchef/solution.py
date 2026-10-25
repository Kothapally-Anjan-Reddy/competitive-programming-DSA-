# cook your dish here

N,M=map(int,input().split())
A=set(map(int,input().split()))

s=[]

for i in range(M):
    x,y,z=input().split()
    s.append((int(x),int(y),z))

# s=sorted(s,key=lambda x:x[1],reverse=True)

# for x,y,z in s:
#     if x in A:
#         print(z)
        
# for x,y,z in s:
#     if x not in A:
#         print(z)

# Instead of writing the above commented code:

s=sorted(s,key=lambda x:(
    x[0] in A,
    x[1]),reverse=True)
    
for x,y,z in s:
    print(z)
