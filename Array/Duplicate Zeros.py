#Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

#Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place
#do not return anything.


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dups = 0
        n = len(arr) - 1
        
        #counting the zeros which are eligible for duplication
        for x in range(n):
            if x > n - dups:
                break
                
            if arr[x] == 0:
                #case where last element of the final array is 0
                if x == n - dups:
                    arr[n] = 0
                    n -= 1
                    break
                    
                dups += 1
                
        last = n - dups
        for i in range(last,-1,-1):
            if arr[i] == 0:
                arr[i + dups] = arr[i]
                dups -= 1
                arr[i + dups] = arr[i]
            else:
                arr[i + dups] = arr[i]
