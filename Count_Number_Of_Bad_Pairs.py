from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = (n * (n - 1)) // 2  # Total possible pairs
        
        freq = defaultdict(int)
        good_pairs = 0
        
        for i, num in enumerate(nums):
            key = num - i  # Calculate the key to check for valid pairs
            good_pairs += freq[key]  # Count good pairs found so far
            freq[key] += 1  # Update frequency of the key
        
        return total_pairs - good_pairs  # Bad pairs = Total pairs - Good pairs
