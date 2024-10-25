class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        length = 1
        end = strs.count(base)
        for i in range(end):
            strs.remove(base)
        if len(strs) == 0:
            return base
        while True:
            output = base[:length]
            for item in strs:
                if item == "":
                    return ""
                else:
                    if item[:length] != output:
                        return output[:-1]
            if length == len(base):
                return output
            length += 1
