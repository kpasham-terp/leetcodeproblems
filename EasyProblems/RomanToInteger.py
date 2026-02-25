class Solution:
    def romanToInt(self, s: str) -> int:
        lookUpTable = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        numeral = 0

        for i in range(len(s)):
            if i + 1 < len(s) and lookUpTable[s[i]] < lookUpTable[s[i+1]]:
                numeral -= lookUpTable[s[i]]
                continue
            numeral += lookUpTable[s[i]]
        return numeral