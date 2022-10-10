class Merge_sort:
    def __init__(self, arr: list):
        self.arr = arr
        self.sort(0, len(self.arr) - 1)

    def sort(self, lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2

        self.sort(lo, mid)
        self.sort(mid + 1, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        i = lo
        j = mid + 1
        aux = self.arr.copy()

        for k in range(lo, hi + 1):
            if i > mid:
                self.arr[k] = aux[j]
                j += 1
            elif j > hi:
                self.arr[k] = aux[i]
                i += 1
            elif aux[j] > aux[i]:
                self.arr[k] = aux[i]
                i += 1
            else:
                self.arr[k] = aux[j]
                j += 1


class Merge_sort_py:
    def __init__(self, arr: list):
        self.arr = arr
        self.arr = self.sort(self.arr)
    def sort(self, arr: list):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])

        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))

        merged += left if left else right

        return merged


class Merge_sort_button:
    def __init__(self, arr: list):
        self.arr = arr
        self.sort(self.arr)

    def sort(self, arr: list):
        sz = 1
        while sz < len(arr):
            lo = 0
            while lo < len(arr) - sz:
                mid = lo + (sz + sz - 1) // 2
                self.merge(lo, mid, min(lo + sz + sz - 1, len(arr) - 1))
                lo += sz + sz
            sz += sz

    def merge(self, lo, mid, hi):
        i = lo
        j = mid + 1
        aux = self.arr.copy()

        for k in range(lo, hi + 1):
            if i > mid:
                self.arr[k] = aux[j]
                j += 1
            elif j > hi:
                self.arr[k] = aux[i]
                i += 1
            elif aux[j] > aux[i]:
                self.arr[k] = aux[i]
                i += 1
            else:
                self.arr[k] = aux[j]
                j += 1


if __name__ == '__main__':
    li = [5, 45, 3, 56, 2, 5, 3, 1, 2, 5, 8, 68, 23, 65, 45, 12, 323, 56, 87, 52, 3, 66, 54, 216, 586, 23, 5866, 1235,
          48]
    merge = Merge_sort_button(li)
    print(merge.arr)
