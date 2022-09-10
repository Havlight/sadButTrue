class Kmp:
    def __init__(self, pattern: str):
        self.p = pattern
        self.next = [0, 0]
        self.build()

    def build(self):
        j = 0
        for i in range(1, len(self.p)):
            while j > 0 and self.p[i] != self.p[j]:
                j = self.next[j]
            if self.p[i] == self.p[j]:
                j += 1
            self.next.append(j)

    def search(self, source: str):
        j = 0
        for i in range(len(source)):
            while j > 0 and self.p[j] != source[i]:
                j = self.next[j]
            if self.p[j] == source[i]:
                j += 1
            if j == len(self.p):
                return i - len(self.p) + 1


if __name__ == '__main__':
    kmp = Kmp('abc')
    print(kmp.search('aaabcde'))
