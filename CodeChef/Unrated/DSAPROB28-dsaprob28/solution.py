def countWays(S):
    # Write your code here
    if S==1:
        return 1
    elif S==2:
        return 2
    else:
        return countWays(S-1) + countWays(S-2)

if __name__ == "__main__":
    S = int(input())
    print(countWays(S))
