'''
1047. Remove All Adjacent Duplicates In String

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"

'''

def solution(s):
    stack = []
    
    # iterate through each character of the string
    for char in s:
        
        # check if stack is not empty and if the character is equal to the last element in the stack
        if stack and char == stack[-1]:
            # if it is then pop out 
            stack.pop()
        else:
            # add character to the stack
            stack.append(char)
    
    # convert the characters into a string        
    return ''.join(stack)
