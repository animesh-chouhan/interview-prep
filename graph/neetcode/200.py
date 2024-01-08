class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # r, c = len(grid), len(grid[0])
        # check = [[False for x in range(c)] for y in range(r)]
        is_visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j):
            # print(i, j)
            # for x in is_visited:
            #     print(x)
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return
            if grid[i][j] == "0":
                return
            if not is_visited[i][j]:
                is_visited[i][j] = True
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not is_visited[i][j] and grid[i][j] == "1":
                    # print(i, j)
                    num_islands += 1
                    dfs(i, j)

        return num_islands


s = Solution()
# print(
#     s.numIslands(
#         grid=[
#             ["1", "1", "1", "1", "0"],
#             ["1", "1", "0", "1", "0"],
#             ["1", "1", "0", "0", "0"],
#             ["0", "0", "0", "0", "0"],
#         ]
#     )
# )
# print(
#     s.numIslands(
#         grid=[
#             ["1", "1", "0", "0", "0"],
#             ["1", "1", "0", "0", "0"],
#             ["0", "0", "1", "0", "0"],
#             ["0", "0", "0", "1", "1"],
#         ]
#     )
# )
print(s.numIslands([["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]]))
