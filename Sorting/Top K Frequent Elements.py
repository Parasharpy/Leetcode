#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#Input1: nums = [1,1,1,2,2,3], k = 2, Output: [1,2]
#Input2: nums = [1], k = 1, Output: [1]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] += 1
        arr = list(mydict.keys())
        start = 0
        end = len(arr)-1
        def select(start, end, k):
            pivot_index = partition(start, end)
            if pivot_index < k:
                return select(pivot_index+1,end,k)
            elif pivot_index > k:
                return select(start,pivot_index-1,k)
            return arr[0:k+1]
        def partition(start,end):
            pivot_index = (start+end)//2
            pivot_freq = mydict[arr[pivot_index]]
            arr[pivot_index],arr[end] = arr[end],arr[pivot_index]
            
            for i in range(start,end):
                if mydict[arr[i]] > pivot_freq:
                    arr[start],arr[i] = arr[i],arr[start]
                    start += 1
            arr[end],arr[start] = arr[start],arr[end]
            return start
        return select(start,end,k-1)
