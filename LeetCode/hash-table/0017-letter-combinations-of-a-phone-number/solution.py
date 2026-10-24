class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        res=[]
        result=[]
        s = [
            ['a', 'b', 'c'],        # Index 0 (Digit 2)
            ['d', 'e', 'f'],        # Index 1 (Digit 3)
            ['g', 'h', 'i'],        # Index 2 (Digit 4)
            ['j', 'k', 'l'],        # Index 3 (Digit 5)
            ['m', 'n', 'o'],        # Index 4 (Digit 6)
            ['p', 'q', 'r', 's'],   # Index 5 (Digit 7)
            ['t', 'u', 'v'],        # Index 6 (Digit 8)
            ['w', 'x', 'y', 'z']    # Index 7 (Digit 9)
        ]

        def dfs(i):
            if i>=len(digits):
                result.append("".join(res.copy()))
                return

            for j in s[int(digits[i])-2]:
                res.append(j)
                dfs(i+1)
                res.pop()

        dfs(0)
        return result
