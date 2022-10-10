class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',           '8': 'tuv', '9': 'wxyz'}
        ans = []
        def dfs(idx=0, path=''):
            if idx > len(digits) - 1:
                ans.append(path)
                return
            cur_words = digit_map.get(digits[idx], '')
            for i in cur_words:
                dfs(idx + 1, path + i)
        dfs()
        return ans
