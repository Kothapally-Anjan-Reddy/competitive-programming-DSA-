def check_square_sum(c):
    # Write your code here
    num=1
    A=set()
    while (num**2)<c:
        A.add(num**2)
        num+=1
        
    for i in A:
        if c-i in A:
            return True
    return False
    
if __name__ == "__main__":
    c = int(input())
    if check_square_sum(c):
        print("true")
    else:
        print("false")
