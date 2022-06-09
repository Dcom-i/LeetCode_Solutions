class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f,l=0,len(numbers)-1
        while f<l:
            sum=numbers[f]+numbers[l]
            if sum > target: l-=1
            elif sum < target: f+=1
            else: return f+1, l+1
