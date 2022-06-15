class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def len_s(e):return len(e)
        words.sort(key=len_s)
        q={}
        for i in words:
            q[i]=1   
            for j in range(len(i)):
                c=i[:j]+i[j+1:] 
                if c in q:
                   q[i]=max(q[i], q[c]+1)

        return max(q.values())
