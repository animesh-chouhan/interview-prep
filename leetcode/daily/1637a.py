class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        pointx = sorted([point[0] for point in points])
        distance = []
        for i in range(len(pointx) - 1):
            distance.append(pointx[i + 1] - pointx[i])

        print(distance)
        return max(distance)
