class Shell_sort:
    def __init__(self, arr: list):
        self.arr = arr
        self.sort(arr)

    def sort(self, arr: list):
        gap = 1
        while gap < (len(arr) // 3):
            gap = 3 * gap + 1
        while gap >= 1:
            for i in range(gap, len(arr)):
                j = i
                while j >= gap and arr[j] < arr[j - gap]:
                    self.swap(j, j - gap)
                    j = j - gap
            gap = gap // 3
    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


if __name__ == '__main__':
    li = [5, 45, 3, 56, 2, 5, 3, 1, 2, 5, 8, 68, 23, 65, 45, 12, 323, 56, 87, 52, 3, 66, 54, 216, 586, 23, 5866, 1235,
          48]
    shell = Shell_sort(li)
    print(shell.arr)
