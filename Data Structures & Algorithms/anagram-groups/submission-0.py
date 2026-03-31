from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        bag_of_words = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            bag_of_words[sorted_word].append(word)
        
        return list(bag_of_words.values())