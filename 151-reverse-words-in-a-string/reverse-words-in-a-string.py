class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip() #the Cleaner
        s=s.split() #the cutter
        s.reverse()
        return " ".join(s)
        