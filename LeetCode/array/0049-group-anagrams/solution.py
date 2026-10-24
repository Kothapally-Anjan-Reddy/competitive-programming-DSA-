class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # small=[]
        # large=[]
        # hashmap={}

        # for word in strs:
        #     st="".join(sorted(word))
        #     hashmap.update({word:st})
        
        # list1=sorted(hashmap.items(), key=lambda x:x[1])
        # recent=list1[0][1]
        # small.append(list1[0][0])

        # for i in list1[1:]:
        #     if i[1]==recent:
        #         small.append(i[0])
        #     else:
        #         large.append(small)
        #         small=[]
        #         small.append(i[0])
        #         recent=i[1]

        # large.append(small)

        # return large


        group={}

        for word in strs:
            st="".join(sorted(word))

            if st not in group:
                group[st]=[]

            group[st].append(word)

        return list(group.values())
