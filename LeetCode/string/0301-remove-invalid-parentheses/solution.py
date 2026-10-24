class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        max_len=-1
        res=set()

        def dfs(i,curr_str,l,r):#->i:pointer, curr_str has list of characters, l,r are left and right paranthesis count
            nonlocal max_len
            if i>=len(s):
                if l==r:
                    if len(curr_str)>max_len:
                        max_len=len(curr_str)
                        res.clear()
                        res.add("".join(curr_str))
                    elif len(curr_str)==max_len:
                        res.add("".join(curr_str))
                return
                
            if s[i]=='(':
                curr_str.append('(')
                dfs(i+1,curr_str,l+1,r)
                curr_str.pop()
                dfs(i+1,curr_str,l,r)
            elif s[i]==')':
                if l>r:
                    curr_str.append(')')
                    dfs(i+1,curr_str,l,r+1)
                    curr_str.pop()
                dfs(i+1,curr_str,l,r)
            else:
                curr_str.append(s[i])
                dfs(i+1,curr_str,l,r)
                curr_str.pop()
        
        dfs(0,[],0,0)
        return list(res)
