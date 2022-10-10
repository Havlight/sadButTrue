class BM:
    def __init__(self, pat: str):
        self.pat = pat
        self.right = {c: i for i, c in enumerate(pat)}

    def search(self, source: str):
        n = len(source)
        m = len(self.pat)
        skip = 1
        for i in range(0, n - m + 1, skip):
            skip = 0
            for j in range(m - 1, -1, -1):
                if self.pat[j] != source[i + j]:
                    skip = j - self.right.get(source[i + j], -1)
                    if skip < 1: skip = 1
                    break
            if skip == 0:
                return i
        return -1


if __name__ == '__main__':
    bm = BM('ccb')
    print(bm.search('abccbac'))
