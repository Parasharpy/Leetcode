#Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
#The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = mini = nums[0]
        for num in nums:
            maxi = max(maxi,num)
            mini = min(mini,num)
            
        def gcd(mini,maxi):
            if mini == 0:
                return maxi
            else:
                return gcd(maxi%mini,mini)
            
            
        return gcd(mini,maxi)
