def largestCommonElement(arr1, arr2):
    # Write your code here
    arr1.sort(reverse=True)
    arr2=set(arr2)
    
    result=-1
    
    for x in arr1:
        if x in arr2:
            return x
        
    
    return -1
