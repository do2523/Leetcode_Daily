# 387. First Unique Character in a String

# O(n) Time
# O(n) Space

'''
First attempt took me 20 minutes because I tried a nested for loop but my logic was off. The solution below took 2 minutes
after I used a hashmap.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        charCount = {}

        for i in range(len(s)):
            charCount[s[i]] = 1 + charCount.get(s[i], 0)
        

        for c in range(len(s)):
            if charCount[s[c]] == 1:
                return c
        
        return -1

