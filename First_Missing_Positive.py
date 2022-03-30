from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = set(nums)
        i = 1
        while i in res:
            i += 1
        return i
