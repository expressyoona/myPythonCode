class Solution:
    def lengthOfLastWord(self, s):
        L = s.split()
        if len(L) == 0:
            return 0
        return len(L[len(L) - 1])
