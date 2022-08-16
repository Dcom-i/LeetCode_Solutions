class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for k, v in count.items():
            if v==1: return int(*[x for x in range(len(s)) if s[x]==k])
        return -1
