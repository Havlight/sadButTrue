def quicksort(alist):
    quicksortHelper(alist, 0, len(alist) - 1)


def quicksortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)

        quicksortHelper(alist, first, splitPoint - 1)
        quicksortHelper(alist, splitPoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


