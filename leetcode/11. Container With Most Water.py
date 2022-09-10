import queue

li = [8, 10, 14, 0, 13, 10, 9, 9, 11, 11]


#   TIE
# class Solution:
#     def maxArea(self, height: list[int]):
#         pq = queue.PriorityQueue()
#         for idx, data in enumerate(height):
#             pq.put((data, idx))
#
#         max_area = 0
#
#         while not pq.empty():
#             h, index = pq.get()
#
#             width = 0
#             for i in range(len(height)):
#                 if height[i] >= h:
#                     width = max(width, abs(i - index))
#             max_area = max(max_area, width * h)
#         return max_area
class Solution:
    def maxArea(self, height: list[int]):
        area = 0
        i = 0
        j = len(height) - 1
        while True:
            if i >= j:
                break
            low_h = min(height[i], height[j])
            area = max(area, low_h * (j - i + 1))

            if low_h == height[i]:
                i += 1
            else:
                j -= 1
        return area
