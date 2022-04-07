class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            slist = sorted(stones)
            big1 = slist[-1]
            big2 = slist[-2]
            if big1==big2:
                stones=slist[:-2]
            else:
                slist.remove(big1)
                slist.remove(big2)
                slist.append(big1-big2)
                stones=slist
        if len(stones)==1:
            return stones[0]
        else:
            return 0
