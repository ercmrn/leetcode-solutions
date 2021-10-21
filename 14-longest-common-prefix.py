class Solution:
    # this one was slower, but used less memory
    def longestCommonPrefix_a(self, strs: List[str]) -> str:        
        if len(strs) == 0:
            return ""

        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for next_string in strs[1:]:
                if i == len(next_string) or c != next_string[i]:
                    return strs[0][:i]
            i += 1
        
        return strs[0]

    # this one was faster, but used more memory
    def longestCommonPrefix_b(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            for next_string in strs[1:]:
                if i == len(next_string) or strs[0][i] != next_string[i]:
                    return strs[0][:i]

        return strs[0]
