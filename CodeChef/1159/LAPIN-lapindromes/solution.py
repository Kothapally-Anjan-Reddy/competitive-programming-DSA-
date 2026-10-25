# cook your dish here

T=int(input())

for i in range(T):
    A=[0]*26
    s=input()
    i=0
    j=len(s)-1
    
    while j>i:
        A[ord(s[i])-97]+=1
        A[ord(s[j])-97]+=-1
        i+=1
        j+=-1
        
    j=1
    
    for i in A:
        if i!=0:
            j=0
            break
    print("YES" if j==1 else "NO")
