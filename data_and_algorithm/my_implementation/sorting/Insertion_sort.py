class Insertion_sort:
    def __init__(self, arr: list):
        self.arr = arr
        self.sort(self.arr)

    def sort(self, arr: list):
        for i in range(1, len(self.arr)):
            j = i
            while j > 0 and self.arr[j] < self.arr[j - 1]:
                self.swap(j, j - 1)
                j -= 1

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


if __name__ == '__main__':
    li = [5, 45, 3, 56, 2, 5, 3, 1, 2, 5, 8, 68, 23]
    insert = Insertion_sort(li)
    print(li)
