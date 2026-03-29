class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {str(sorted(strs[0])):[]}
        for i in strs:
            key = str(sorted(i))
            if key in hashmap.keys():
                l = hashmap[key]
                l.append(i)
                hashmap[key] = l
            else:
                hashmap[key] = [i]
        l = [] 
        for i in hashmap.values():
            l.append(i)
        return l

