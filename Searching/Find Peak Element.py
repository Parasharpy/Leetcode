#A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, and return its index. 
#If the array contains multiple peaks, return the index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞.
#Input: nums = [1,2,1,3,5,6,4], output: 5

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while end > start:
            mid = (start+end)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid + 1
        return (start+end)//2
