class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        count_nums = set()

        for num in nums:
            if num in count_nums:
                return num
            else:
                count_nums.add(num)