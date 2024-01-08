class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted([point[0] for point in points])
        max_distance = 0
        for i in range(len(points) - 1):
            if points[i + 1] - points[i] > max_distance:
                max_distance = points[i + 1] - points[i]
        return max_distance
