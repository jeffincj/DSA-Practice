class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        #start the first string as the potential prefix
        prefix = strs[0]
        for s in strs[1:]:
            #while the current string doesn't start with the prefix
            while not s.startswith(prefix):
                #shorten the prefix by one character from the end
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
