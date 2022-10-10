import math


class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     ans = math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))
    #     return ans

    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    path[i][j] = 1
                else:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[m - 1][n - 1]


s = Solution()
print(s.uniquePaths(3, 7))
