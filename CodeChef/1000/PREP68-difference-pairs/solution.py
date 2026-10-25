def hasPairWithDifference(A: list[int], N: int, B: int) -> int:
    # write your code here 
    presence=set()
    
    for x in A:
        if x-B in presence or x+B in presence:
            return 1
        else:
            presence.add(x)
            
    return 0
