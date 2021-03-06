'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left<right:
            if not s[left].isalnum():
                left +=1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].upper()==s[right].upper():
                left+=1
                right-=1
            else:
                return False
        return True
