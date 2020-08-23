# link : https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxh = []  
        self.minh = []        

    def addNum(self, num: int) -> None:
        heappush(self.maxh, -num) 
        heappush(self.minh, -self.maxh[0])
        heappop(self.maxh)
        
        if len(self.maxh) < len(self.minh):
            heappush(self.maxh, -self.minh[0])
            heappop(self.minh)

    def findMedian(self) -> float:
        if len(self.maxh) > len(self.minh):
            return -self.maxh[0]                  
        else:
            return (self.minh[0] - self.maxh[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()