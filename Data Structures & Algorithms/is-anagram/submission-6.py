class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            t = list(t)
            for i in s:
                if i in t:
                    t.remove(i)
            if len(t) == 0:
                return True
            else: 
                return False
        else: 
            return False
        