"""
        ## RC ##
        ## APPROACH : 2 HEAPS ##
        ## LOGIC ##
        ## One minheap to store low values and second maxheap to store max values, we keep track and update median every time after insertion ##
        
		## TIME COMPLEXITY : O(logN) ##
		## SPACE COMPLEXITY : O(N) ##
BETTER TO UNDERSTAND IF lo is understood as left side and hi as right side 
        ## EXAMPLE ##
        Adding number 41
        MaxHeap lo: [41]// MaxHeap stores the largest value at the top (index 0)
        MinHeap hi: []// MinHeap stores the smallest value at the top (index 0)
        Median is 41
        =======================
        Adding number 35
        MaxHeap lo: [35] // max heap stores smaller half of nums
        MinHeap hi: [41] // min heap stores bigger half of nums
        Median is 38
        =======================
        Adding number 62
        MaxHeap lo: [41, 35]
        MinHeap hi: [62]
        Median is 41
        =======================
        Adding number 4
        MaxHeap lo: [35, 4]
        MinHeap hi: [41, 62]
        Median is 38
        =======================
        Adding number 97
        MaxHeap lo: [41, 35, 4]
        MinHeap hi: [62, 97]
        Median is 41
        =======================
        Adding number 108
        MaxHeap lo: [41, 35, 4]
        MinHeap hi: [62, 97, 108]
        Median is 51.5
"""

class MedianFinder:
    def __init__(self):
        self.left=[]##need to access 0th index ,so descending
        self.right=[]
	##              \
        ##        right  \  
        ##       median   --- \
        ##         left        \

    def addNum(self, num: int) -> None:
        heappush(self.left,-num)  # is maxheap, so -1 * num
        heappush(self.right,-self.left[0]) #is minheap
	## pop the value added to right
        heappop(self.left)
	##  This ensures that the left heap contains the smaller half of the numbers, and the right heap contains the larger half.If the size 
	## of left becomes greater than the size of right, the largest element from left is moved to right to balance the heaps.
        if len(self.left)<len(self.right):
            heappush(self.left,-self.right[0])
	    ## pop the value added to left
            heappop(self.right)

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -self.left[0]
        else:
            return (self.right[0]-self.left[0])/2 # - as left has -ve values
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
