class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        else:
            # count=0
            # for i in range(0,n+1):
            #     for j in range(0,(n//2)+1):
            #         if (i + (j*2))==n:
            #             ways=int((factorial(i+j))/(factorial(i)*factorial(j)))
            #             count+=ways

            # return count

            # The soln is correct but not optimal as there are two loops and heavy computations.




            # def fib(n):
            #     if n==1: return 1
            #     elif n==2: return 2
            #     else:
            #         return fib(n-1)+fib(n-2)

            # return fib(n)

            # This results in the tle thing as it computes a simgle thing multiple times so, to 
            # avoid it use DP or use the below method

            def fib(n):
                if n==1: return 1
                elif n==2: return 2
                else:
                    a,b=1,2
                    for _ in range(3,n+1):
                        a,b=b,a+b
                    return b
            return fib(n)
