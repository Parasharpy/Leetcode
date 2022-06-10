#You are playing the Bulls and Cows game with your friend.

#You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess,
#you provide a hint with the following info:

#The number of "bulls", which are digits in the guess that are in the correct position.
#The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
#Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

#The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and 
#guess may contain duplicate digits.


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bulls = cows = 0
        bull_dict = {}
        for i in range(n):
            if secret[i] == guess[i]:
                if secret[i] not in bull_dict:
                    bull_dict[secret[i]] = 1
                else:
                    bull_dict[secret[i]] += 1
                bulls += 1
        dictt = {}
        mapp = {}
        for x in secret:
            if x not in dictt:
                dictt[x] = 1
            else:
                dictt[x] += 1
        for x in guess:
            if x not in mapp:
                mapp[x] = 1
            else:
                mapp[x] += 1
        for x in mapp.keys():
            if x in dictt:
                if dictt[x] < mapp[x]:
                    cows += dictt[x]
                else:
                    cows += mapp[x]
                if x in bull_dict:
                    cows -= bull_dict[x]
        return str(bulls) + "A" + str(cows) + "B"
