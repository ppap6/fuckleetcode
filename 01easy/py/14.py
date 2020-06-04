'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
'''



# 使用zip()
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in zip(*strs):
            if len(set(i))==1:
                res += i[0]
            else:
                break
        return res

# 硬着头皮写：
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):return ""
        if len(strs) ==1 : return strs[0]
        n = len(strs[0])
        s= set()
        ll = set()
        for i in range(n):
            s.add(strs[0][:i+1])
        for t in strs:
            for tmp in s:
                if t.startswith(tmp):
                    continue
                else:
                    ll.add(tmp)
        s = s-ll
        if not s:
            return ""
        else:
            max_ = 0
            for m in s:
                max_ = max(max_, len(m))
        for m in s:
            if len(m)==max_:
                return m
