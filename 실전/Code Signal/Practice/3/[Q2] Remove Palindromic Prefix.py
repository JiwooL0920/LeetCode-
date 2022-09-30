# You are given a string s. Consider the following algorithm applied to this string:

# Take all the prefixes of the string, and choose the longest palindrome between them.
# If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

# Example

# For s = "aaacodedoc", the output should be solution(s) = "".

# The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
# Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
# Finally the algorithm ends on the empty string, so the answer is "".
# For s = "codesignal", the output should be solution(s) = "codesignal".
# The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

# For s = "", the output should be solution(s) = "".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string consisting of English lowercase letters.

# Guaranteed constraints:
# 0 ≤ s.length ≤ 1000.

# [output] string

# The result of the described algorithm.

def solution(s):

    def isPalindrome(s):
        l, r = 0, len(s)-1 
        while l <= r:
            if s[l] != s[r]:
                return False 
            l += 1 
            r -= 1 
        return True 
        
    i = 0
    length = len(s)
    while i <= length:
        j = i+1
        longestPalindromicSubstring = ""
        cutIndex = 0
        while j <= length:
            substring = s[:j] 
            if isPalindrome(substring):
                longestPalindromicSubstring = substring 
                cutIndex = j 
            j += 1
        if len(longestPalindromicSubstring) > 1:
            length -= len(longestPalindromicSubstring)
            s = s[cutIndex:]
        i += 1
    return s
            
