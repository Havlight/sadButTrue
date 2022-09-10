class Quick_sort:
    def __init__(self, arr: list):
        self.arr = arr
        self.sort(0, len(arr) - 1)

    def sort(self, lo, hi):
        if hi <= lo: return

        j = self.partition(lo, hi)
        self.sort(lo, j - 1)
        self.sort(j + 1, hi)

    def partition(self, lo, hi):
        k = self.arr[lo]
        i = lo + 1
        j = hi
        while True:
            while self.arr[i] <= k:
                if i == hi: break
                i += 1
            while self.arr[j] >= k:
                if j == lo: break
                j -= 1
            if i >= j: break
            self.swap(i, j)
        self.swap(lo, j)
        return j

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


class Quick_sort_3way:
    def __init__(self, arr: list):
        self.arr = arr
        self.sort(0, len(arr) - 1)

    def sort(self, lo, hi):
        if lo >= hi: return
        it = lo
        gt = hi
        i = lo + 1

        v = self.arr[lo]

        while i <= gt:
            if self.arr[i] < v:
                self.swap(i, it)
                it += 1
                i += 1
            elif self.arr[i] > v:
                self.swap(i, gt)
                gt -= 1
            else:
                i += 1
        self.sort(lo, it - 1)
        self.sort(gt + 1, hi)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


class Quick_3_string:
    def __init__(self, arr: list[str]):
        self.arr = arr
        self.sort(0, len(arr) - 1, 0)

    def sort(self, lo, hi, idx):
        if lo >= hi: return
        it = lo
        gt = hi
        ch = self.get_ch(lo, idx)
        i = lo + 1
        while i <= gt:
            t = self.get_ch(i, idx)
            if t < ch:
                self.swap(i, it)
                it += 1
                i += 1
            elif t > ch:
                self.swap(i, gt)
                gt -= 1
            else:
                i += 1
        self.sort(lo, it - 1, idx)
        if ch > 0: self.sort(it, gt, idx + 1)
        self.sort(gt + 1, hi, idx)

    def get_ch(self, lo, idx):
        try:
            ch = self.arr[lo][idx]
            return ord(ch)
        except:
            return -1

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


if __name__ == '__main__':
    li = input('array is:').split()
    sort = Quick_3_string(li)
    print(li)

