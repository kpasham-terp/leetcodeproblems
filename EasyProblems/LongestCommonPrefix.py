class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        min_length = min(len(s) for s in strs)
        if min_length == 0:
            return ""
        print(min_length)
        for i in range(min_length):
            currChar = strs[0][i]
            j = 0
            while j < len(strs):
                if strs[j][i] != currChar:
                    return pre
                j = j + 1
            pre = pre + currChar
        return pre