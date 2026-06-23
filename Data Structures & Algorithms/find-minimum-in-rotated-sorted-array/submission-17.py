class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        
        i = 0
        if nums[l]<= nums[r]:
            return nums[l]

        while l <= r:             
            m = (l+r)//2

            if m <r and nums[m] > nums[m+1]:
                return nums[m+1]
            elif m > l and nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] >= nums[l]:
                l = m +1
            else:
                r = m -1
        return nums[0]
        

