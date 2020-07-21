# 递归解法，容易超时，python可以加个缓存装饰器，这样也算是将递归转换成迭代的形式了
class Solution:
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# DP，新建一个字典或者数组来存储以前的变量，空间复杂度O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 还是DP，只不过是只存储前两个元素，减少了空间，空间复杂度O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        fst = 1
        sec = 2
        res = 0
        for i in range(2, n):
            res = fst + sec
            fst = sec
            sec = res
        return max(n , res)  # 使用max针对n=2和n=1的情况，这时候就取n就好了。

# 直接斐波那契数列的计算公式喽
class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        sqrt5=5**0.5
        fibin=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
        return int(fibin/sqrt5)
