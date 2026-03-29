class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = 0
        for i in range(len(nums)):
            pair = (target - nums[i])
            if pair in nums:
                if i != nums.index(pair,i):
                    return [i,nums.index(pair)]
                else:
                    try:
                        return [i,nums.index(pair,i+1)]
                    except:
                        pass

            else: 
                pass
        return