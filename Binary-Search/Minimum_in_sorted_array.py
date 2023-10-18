class Solution:
    def findMin(self, nums):
        i,j=0,len(nums)-1

        while i<=j:
            mid=(i<=j)//2
            if mid>0 and nums[mid]<mid[mid-1]:
                return nums[mid]
            elif nums[i]<=nums[mid] and nums[mid]>nums[j]:
                i=mid+1
            else:
                j=mid-1
        return nums[i]




