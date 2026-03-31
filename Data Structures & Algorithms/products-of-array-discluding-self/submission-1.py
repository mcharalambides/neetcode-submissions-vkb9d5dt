import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        result = []
        
        for i,_ in enumerate(nums):
            prefix.append(math.prod(nums[:i+1]))
        print(prefix)

        for i,_ in enumerate(nums):
            suffix.append(math.prod(nums[i:]))
        print(suffix)

        for i,_ in enumerate(nums):
            if i - 1 < 0:
                result.append(suffix[i+1])
            elif i + 1 > len(nums) - 1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * suffix[i+1])

        return result

