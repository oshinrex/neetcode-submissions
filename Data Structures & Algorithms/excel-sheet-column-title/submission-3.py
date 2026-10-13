class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber:
            columnNumber -= 1
            curr = columnNumber % 26
            res.append(chr(curr + ord('A')))
            columnNumber //= 26
            print(columnNumber)
        
        return "".join(res[::-1])