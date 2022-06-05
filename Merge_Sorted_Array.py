class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        while m+n<len(nums1):
            nums1.remove(0)
        #################################
        # temp=[]
        # for i in range(0,m):
        #     temp.append(nums1[i])
        # nums1.clear()
        # for j in range(0,n):
        #     temp.append(nums2[j])
        # nums1 =  sorted(temp) 
