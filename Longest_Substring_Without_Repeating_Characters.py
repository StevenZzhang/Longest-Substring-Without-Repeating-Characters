class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        n = len(s)
        res = left  = right = 0
        m = {}
        while right < n:      
            c = s[right]      
            if c in  m and m[c] >= left :
                left = m[c] + 1
            res = max(res, right -left  + 1)
            m[c] = right
            right += 1
        return res
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = left  =  0
        m = {}
        for right in range(n):      
            c = s[right]      
            if c in  m and m[c] >= left :
                left = m[c] + 1
            res = max(res, right -left  + 1)
            m[c] = right
           
        return res
