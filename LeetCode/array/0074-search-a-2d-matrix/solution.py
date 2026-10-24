class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        def binary(l,r,arr):
            if l>r:
                return False
            m=(l+r)//2
            if arr[m]==target:
                return True
            elif arr[m]>target:
                return binary(l,m-1,arr)
            else:
                return binary(m+1,r,arr)
        def binary_mat(l,r):
            if l>r:
                return False
            m=(l+r)//2
            if matrix[m][0]<=target and matrix[m][-1]>=target:
                return binary(0,len(matrix[0]),matrix[m])
            elif matrix[m][0]>target:
                return binary_mat(l,m-1)
            else:
                return binary_mat(m+1,r)

        return binary_mat(l,r)
