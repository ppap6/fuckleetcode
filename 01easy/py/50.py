'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
'''

# 太慢了：6472 ms	13.8 MB
class Solution:
    def firstUniqChar(self, s: str) -> str:
        for i in s:
            if s.count(i) == 1:
                return i
        return " "

# 优化：
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = not i in dic
        for k, v in dic.items():
            if v: return k
        return " "
