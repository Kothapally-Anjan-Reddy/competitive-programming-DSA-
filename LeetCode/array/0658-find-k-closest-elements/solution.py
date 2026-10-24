class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr)<=k:
            return arr
        elif x<arr[0]:
            return arr[:k]
        elif x>arr[-1]:
            return arr[len(arr)-k:]
        else:
            mini_i=0
            for i,n in enumerate(arr):
                if n<x:
                    continue
                if n==x:
                    mini_i=i
                    break
                else:
                    if abs(arr[i-1]-x)>abs(arr[i]-x):
                        mini_i=i
                    else:
                        mini_i=i-1
                    break

        p=mini_i+k
        while p>=len(arr):
            p-=1
        q=mini_i-k
        while q<0:
            q+=1
        if arr[p]==arr[q]:
            return [arr[p]]*k
        count=p-q+1
        while count>k:
            if abs(arr[p]-x)<abs(arr[q]-x):
                q+=1
                count-=1
            else:
                p-=1
                count-=1
        return arr[q:p+1]
