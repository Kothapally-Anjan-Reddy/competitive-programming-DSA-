class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        root=TrieNode()
        res=[]
        # Building the Trie Tree:
        for word in wordDict:
            curr=root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.endOfWord=True
        
        # Searching for the string:

        memo=[None]*len(s)

        def search(i):
            if i==len(s):
                return True
            
            if memo[i] is not None:
                return memo[i]
            
            curr=root
            for j in range(i,len(s)):
                if s[j] not in curr.children:
                    break
                curr=curr.children[s[j]]
                if curr.endOfWord==True and search(j+1):
                    memo[i]=True
                    return True
            memo[i]=False
            return False
            
        return search(0)
