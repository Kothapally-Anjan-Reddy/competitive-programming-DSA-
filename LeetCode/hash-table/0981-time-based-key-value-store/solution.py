class TimeMap:

    def __init__(self):
        self.timeMap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap.setdefault(key,[]).append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:  
            arr=self.timeMap[key]       
            l=0
            r=len(arr)-1
            while l<=r:
                m=(l+r)//2
                if arr[m][1]==timestamp:
                    return arr[m][0]
                if arr[m][1]>timestamp:
                    r=m-1
                else:
                    l=m+1
            if arr and arr[0][1]<timestamp:
                return arr[r][0]
            
        return ""       


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
