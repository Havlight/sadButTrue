class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_ps(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l + 1

        max_len = 0
        start = 0

        for i in range(len(s)):
            tmp = max(get_ps(i, i), get_ps(i, i + 1))
            if tmp > max_len:
                max_len = tmp
                start = i - (max_len - 1) // 2
        return s[start:start + max_len]


s = Solution()
print(s.longestPalindrome('abdabac'))
