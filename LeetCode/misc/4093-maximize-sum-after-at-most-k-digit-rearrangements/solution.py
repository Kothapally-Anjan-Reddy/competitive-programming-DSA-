class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        res=0
        arr=[]
        id={}
        for num in nums:
            val=int("".join(sorted(str(num),reverse=True)))
            arr.append((val-num,val,num))
        arr.sort(reverse=True,key=lambda x:x[0])
        for dup in arr:
            if k>0 and dup[1]>dup[2]:
                k-=1
                res+=dup[1]
                print(dup[1])
            else:
                res+=dup[2]
                print(dup[2])

        return res
