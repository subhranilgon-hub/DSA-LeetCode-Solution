class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s= "".join(map(str,digits))
        val= int(s) + 1
        return [int(char) for char in str(val)]
        