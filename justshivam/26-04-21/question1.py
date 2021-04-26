class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ind, cur, l = 0, '', len(min(strs))
        while True:
            if l == ind:
                break
            cur = strs[0][ind]
            for i in strs:
                if i[ind] != cur:
                    return "" if ind == 0 else strs[0][:ind]
            ind += 1
        return strs[0][:ind] if not l == 0 else ""
