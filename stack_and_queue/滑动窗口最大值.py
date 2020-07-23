#MaxHeap
#时间复杂度O(nlogn), remove O(1), push is O(n)
#空间复杂度O(n)
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        res = []
        h = []
        heapq.heapify(h)
        
        for i in range(len(nums)):
            if len(h) < k:
                heapq.heappush(h, -nums[i])
                if len(h) == k:
                    res.append(-h[0])
            else:
                h.remove(-nums[i-k])    # destroy the heap structure, need to heapify again
                heapq.heapify(h)
                heapq.heappush(h, -nums[i])
                res.append(-h[0])
        return res
        
        
# Deque
# 时间、空间复杂度都是O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deque and deque[0] <= i - k: deque.popleft() # outdate indices
            while deque and num > nums[deque[-1]]: deque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res 
