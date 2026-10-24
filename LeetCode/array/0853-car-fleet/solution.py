class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:       
        if len(position)==1:
            return 1
        stack=[]
        # car={}
        # for i,n in enumerate(position):
        #     car[target-n]=speed[i]

        # car=sorted(car.items(),key=lambda x:x[0],reverse=True)
        # car=[x/s for x,s in car[::-1]]
        # print(car)
        car=sorted(zip(position,speed),reverse=True)

        for pos,spe in car:
            time=(target-pos)/spe
            if stack and time<=stack[-1]:
                continue
            stack.append(time)

        return len(stack)
