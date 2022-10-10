class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        arr = []

        def generate(arr, lp=0, rp=0):
            if len(arr) == n * 2:
                ans.append(''.join(arr))
                return
            if lp < n:
                arr.append('(')
                generate(arr, lp + 1, rp)
                arr.pop()
            if rp < lp:
                arr.append(')')
                generate(arr, lp, rp + 1)
                arr.pop()
        generate(arr)

        return ans
    # def generateParenthesis(self, n: int) -> list[str]:
    #     level = 2 * n
    #     pairs = []
    #     pair = []
    #
    #     class BTree:
    #         def __init__(self, val):
    #             self.val = val
    #             self.r = None
    #             self.l = None
    #
    #     def generate_list(level):
    #         li = []
    #         for i in range(level):
    #             for j in range(2 ** i):
    #                 if j % 2 == 0:
    #                     li.append('(')
    #                 else:
    #                     li.append(')')
    #         return li
    #
    #     def generate_tree(items):
    #         n = len(items)
    #
    #         def inner(index=0):
    #             if n <= index:
    #                 return None
    #             node = BTree(items[index])
    #             node.l = inner(2 * index + 1)
    #             node.r = inner(2 * index + 2)
    #             return node
    #
    #         return inner()
    #
    #     root = generate_tree(generate_list(level))
    #
    #     def pre(node, pair):
    #         if node:
    #             pair.append(node.val)
    #             if len(pair) == level:
    #                 pairs.append(pair)
    #
    #             pre(node.l, pair)
    #             if node.l and pair:
    #                 pair.pop()
    #             pre(node.r, pair)
    #             if node.r and pair:
    #                 pair.pop()
    #
    #
    #     pre(root, pair)
    #     return pairs
