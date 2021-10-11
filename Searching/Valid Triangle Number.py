#Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#Input: nums = [2,2,3,4], Output: 3. Explanation: Valid combinations are: 2,3,4 (using the first 2) 2,3,4 (using the second 2) and, 2,2,3
#Input: nums = [4,2,3,4], Output: 4

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1,len(nums)-1):
                while k < len(nums) and (nums[i]+nums[j]) > nums[k]:
                    k += 1
                count += (k-j-1)
        return count
