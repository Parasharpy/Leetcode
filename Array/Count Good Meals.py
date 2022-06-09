#A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

#You can pick any two different foods to make a good meal.

#Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the ith item of food,
#return the number of different good meals you can make from this list modulo 10^9 + 7.

#Note that items with different indices are considered different even if they have the same deliciousness value.



class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dictt = {}
        count = 0
        for i in range(0,22):
            dictt[2**i] = 1
        for j in dictt.keys():
            target = j
            mapp = {}
            for i in range(len(deliciousness)):
                x = target - deliciousness[i]
                if x in mapp:
                    count += mapp[x]
                if deliciousness[i] not in mapp:
                    mapp[deliciousness[i]] = 1
                else:
                    mapp[deliciousness[i]] += 1
        return count % (10**9 + 7)
