def sortArrayByParity(nums):
    # Write your code here
    left=0
    right=len(nums)-1
    A=[0]*len(nums)
    # def find_even(pos):
    #     while pos<len(nums) and nums[pos]%2!=0:
    #         pos+=1
    #     return pos if pos<len(nums) else -1
    
    # def find_odd(pos):
    #     while pos<len(nums) and nums[pos]%2==0:
    #         pos+=1
    #     return pos if pos<len(nums) else -1
    
    # while p1<len(nums):
    #     p1=find_even(p1)
    #     p2=find_odd(p1+1)
    #     if p1==-1 or p2==-1:
    #         break
    #     x=nums.pop(p2)
    #     nums.insert(p1,x)
    
    for x in nums:
        if x%2!=0:
            A[left]=x
            left+=1
        else:
            A[right]=x
            right-=1
            
    right=len(nums)-1
    
    while left<right:
        A[left],A[right]=A[right],A[left]
        left+=1
        right-=1
    
    return A

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    A=sortArrayByParity(nums)

    print(" ".join(map(str, A)))
