class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        right = {i: idx for idx, i in enumerate(needle)}

        def bm():
            s_len = len(haystack)
            p_len = len(needle)
            skip = 1

            for i in range(0, s_len - p_len + 1, skip):
                skip = 0
                for j in range(p_len - 1, -1, -1):
                    if needle[j] != haystack[i + j]:
                        skip = j - right.get(haystack[i+j], -1)
                        if skip < 1:
                            skip = 1
                        break
                if skip == 0:
                    return i
            return -1
        return bm()

s = Solution()
print(s.strStr('abccbac', 'ccb'))