'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

def isAnagram(s: str, t: str):
    # check length of s and t
    if len(s) != len(t):
        return False
    
    # create hashmaps to keep track of occurrences of each letter in s and t
    hashmapS, hashmapT = {}, {}
    
    # iterate through map s
    for i in range(len(s)):
        # count each character in string s and once we see that character increment count by 1
        # get function returns the values of the key
        hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
        # print(hashmapS[s[i]])

        hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        # print(hashmapT[t[i]])
    
    # iterate through map and make sure counts are the same
    for c in hashmapS:
        if hashmapS[c] != hashmapT.get(c, 0):
            return False
    
    return True

s = "anagram"
t = "nagaram"
    
print(isAnagram(s, t))    
