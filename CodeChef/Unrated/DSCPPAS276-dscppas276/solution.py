def valid_palindrome(s):
    # Write your code here
    left=0
    right=len(s)-1
    res=True
    
    def palindrome(left: int,right: int):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            res= (palindrome(left+1,right) or palindrome(left,right-1))
            break
    
    return res
    

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    print("true" if valid_palindrome(s) else "false")
