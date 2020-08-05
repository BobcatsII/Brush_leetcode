#光头哥
class Solution:
    ugly = sorted(2**a * 3**b * 5**c  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        return self.ugly[n-1]

#优质解 DP
#由于丑数是质因数只有2，3，5的数（1除外）。 因此丑数可以定义为2^x * 3 ^ y * 5 ^ z。

# 定义三种状态：
# 最后一个乘的质因数是2
# 最后一个乘的质因数是3
# 最后一个乘的质因数是5
# 为了简单起见，我们定义三个指针，分别指向上一个乘的质因数是2, 乘的质因数是3, 乘的质因数是5的位置。
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        states = [1] * n
        p1 = p2 = p3 = 0

        for i in range(1, n):
            states[i] = ith =  min(states[p1] * 2, states[p2] * 3, states[p3] * 5)
            if ith == states[p1] * 2: p1 += 1
            if ith == states[p2] * 3: p2 += 1
            if ith == states[p3] * 5: p3 += 1
        return states[-1]