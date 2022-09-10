class Selection_sort:
    def __init__(self, arr: list):
        self.arr = arr
        self.sort(self.arr)

    def sort(self, arr: list):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]: min_idx = j
            self.swap(i, min_idx)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


if __name__ == '__main__':
    li = [5, 45, 3, 56, 2, 5, 3, 1, 2, 5, 8, 68, 23]
    select = Selection_sort(li)
    print(li)
