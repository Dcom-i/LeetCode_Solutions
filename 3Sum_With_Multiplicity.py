from typing import List
from collections import Counter
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = 0
        nums = Counter(arr[:1])
        for i in range(1, len(arr)-1):
            for j in range(i + 1, len(arr)):
                c = (c + nums[target - arr[j] - arr[i]]) % (10**9+7)
            nums[arr[i]] += 1
        return c
