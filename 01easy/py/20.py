
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
输入: "()[]{}"
输出: true
输入: "{[]}"
输出: true
输入: "([)]"
输出: false
'''
# 解决：使用栈

class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "[":"]", "{":"}"}
        l = []
        for i in s:
            if i in d:
                l.append(i)
            else:
                tmp = d[l.pop()] if l else "#"
                if i != tmp:
                    return False
        return not l