# 一行搞定：利用python的3.8.0的特性  :=  赋值
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if (k := k % len(nums)): nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]


# 切片拼接 O（1）
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]



# 插入
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())

# 三个反转
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1] 
