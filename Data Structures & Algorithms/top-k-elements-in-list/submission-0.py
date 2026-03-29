class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        dct[nums[0]] = 0
        for i in nums:
            if i in dct.keys():
                dct[i] = dct[i] + 1
            else:
                dct[i] = 1
        keys_l = list(dct.keys())
        vals_l = list(dct.values())
        l = []
        for i in range(k):
            max_inx = vals_l.index(max(vals_l))
            l.append(keys_l[max_inx])
            del keys_l[max_inx]
            del vals_l[max_inx]
        return l
        