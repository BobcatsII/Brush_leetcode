#简单解法：
class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]

#双指针法
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
