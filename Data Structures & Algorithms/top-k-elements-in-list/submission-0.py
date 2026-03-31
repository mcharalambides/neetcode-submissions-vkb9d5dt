class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict.fromkeys(set(nums), 0)

        for num in nums:
            counter[num] += 1
        
        result = sorted(counter, key=counter.get, reverse=True)[:k]

        return result