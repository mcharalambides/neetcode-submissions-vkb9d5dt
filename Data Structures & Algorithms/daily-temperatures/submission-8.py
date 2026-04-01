class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        indexes = []
        result = [0] * n

        for i in range(n):
            while indexes and temperatures[i] > temperatures[indexes[-1]]:
                index = indexes.pop()
                result[index] = i - index
            indexes.append(i)
        return result