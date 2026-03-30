class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        pop = 0
        for i in range(len(nums)):
            pop = l.pop(i)
            l = [x * nums[i] for x in l]
            l.insert(i,pop)
        return l
        



#thislist.insert(1, "orange")