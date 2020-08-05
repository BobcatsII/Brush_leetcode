class Solution:
    def maxSlidingWindow(self, nums, k):
        deque = collections.deque()
        res = []
        for i, n in enumerate(nums):
            while deque and nums[deque[-1]] < n:
                deque.pop()
            #deque += i,   #这种是特殊写法
            deque.append(i)
            if deque[0] == i - k:
                deque.popleft()
            if i >= k - 1:
                #res += nums[deque[0]],   #这种是特殊写法
                res.append(nums[deque[0]])
        return res