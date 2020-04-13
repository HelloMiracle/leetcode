class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,-1
        while i<len(nums):
            if i==0:
                j+=1
                i+=1
            else:
                if nums[i]>nums[j]:
                    nums[j+1]=nums[i]
                    j+=1
                i+=1
        return j+1