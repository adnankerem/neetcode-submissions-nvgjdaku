class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            key = str(sorted(i))
            if not hashmap:
                hashmap[key] = [i]
            else:
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

