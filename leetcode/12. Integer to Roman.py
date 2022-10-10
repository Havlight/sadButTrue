class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'),
                  (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]

        roman_map = dict(symbol)
        digits = len(str(num))
        idx = 12
        ans = ''
        while num >= 0 and idx >= 0:
            while num - symbol[idx][0] < 0 and idx >= 0:
                idx -= 1
            num -= symbol[idx][0]
            ans += symbol[idx][1]
        return ans[:-1]

s = Solution()
print(s.intToRoman(1994))

# symbol = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (14, 'XIV'), (19, 'XIX'), (40, 'XL'), (50, 'L'),
#           (90, 'XC'), (99, 'XCIX'), (100, 'C'), (199, 'CXCIX'),
#           (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
