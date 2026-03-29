class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            key = str(sorted(i))
            if key in hashmap.keys():
                hashmap[key].append(i)
            else:
                hashmap[key] = [i]
        l = []
        for i in hashmap.values():
            l.append(i)
        return l