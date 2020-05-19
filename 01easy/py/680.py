'''给定一个非空字符串 s，最多删除一个字符。
判断是否能成为回文字符串。

输入: "abca"
输出: True
解释: 你可以删除c字符。
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        IsTrue = lambda s: s == s[::-1]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return IsTrue(s[left+1:right+1]) or IsTrue(s[left:right])

        return True