class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for i in range(len(s)):
            if s[i].isalnum():
                word.append(s[i].lower())
        return (word == word[::-1])