# 5. longest-palindromic-substring/
# US

# O(n^2) Time
# O(n) Space

'''
40 minutes of me doing my best lol. 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        l, r = 0, len(s) - 1

        while l <= r:
            for i in range(l, len(s)):
                for j in range(i+ 1, r):
                    print("normal: " + s[i:j] +"   reverse: " + s[i:j][::-1])                    
                    if s[i:j] == s[i:j][::-1] and (len(s[i:j]) > len(longest)):
                        longest = s[i:j]

            
            for i in range(len(s), l, -1):
                for j in range(r, l+1, -1):
                    print("normal: " + s[i:j] +"   reverse: " + s[i:j][::-1])                    
                    if s[i:j] == s[i:j][::-1] and (len(s[i:j]) > len(longest)):
                        longest = s[i:j]

            l += 1
            r -= 1


        return longest