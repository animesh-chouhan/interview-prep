from queue import Queue


# finding groups dfs
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        is_visited = [False] * len(isConnected)
        groups = [0] * len(isConnected)

        def visit(node, group):
            for i, j in enumerate(isConnected[node]):
                if j == 1 and not is_visited[i]:
                    is_visited[i] = True
                    groups[i] = group
                    visit(i, group)

        for i in range(len(isConnected)):
            visit(i, i)

        # print(is_visited)
        # print(groups)
        return len(set(groups))


# only counting groups dfs
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        is_visited = [False] * len(isConnected)

        def visit(node):
            for i, j in enumerate(isConnected[node]):
                if j == 1 and not is_visited[i]:
                    is_visited[i] = True
                    visit(i)

        groups = 0
        for i in range(len(isConnected)):
            if not is_visited[i]:
                groups += 1
                visit(i)

        # print(is_visited)
        # print(groups)
        return groups


# bfs
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        is_visited = [False] * len(isConnected)

        def bfs(node):
            q = Queue()
            q.put(node)

            while not q.empty():
                for i, j in enumerate(isConnected[q.get_nowait()]):
                    if j == 1 and not is_visited[i]:
                        q.put(i)
                        is_visited[i] = True

        groups = 0
        for i, j in enumerate(isConnected):
            if not is_visited[i]:
                groups += 1
                bfs(i)

        return groups


s = Solution()
print(s.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
