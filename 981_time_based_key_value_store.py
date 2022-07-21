class TimeMap:
    # input: key -> str; value -> str; timestamp -> int
    # output: the value in the data structure for get -> str

    # constraints:
    # key.length and value.length >= 1
    # key and value contain lower case english and digits
    # the timestamp using set is strictly increasing

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.hashMap:
            self.hashMap[key].append((timestamp, value))
        else:
            self.hashMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        
        result = (-1, "")

        if key not in self.hashMap:
            return result[1]
        
        valueList = self.hashMap[key]
        l, r = 0, len(valueList) - 1
               
        while l <= r:
            
            mid = (l + r) // 2

            if valueList[mid][0] <= timestamp:
                result = valueList[mid]
                l = mid + 1
            elif valueList[mid][0] > timestamp:
                r = mid - 1

        return result[1] 

    # TC: O(logN) for get and O(1) for set
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)