class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = 0 + 0j
        visited = {pos}
        for d in path:
            # print(pos)
            match d:
                case "N":
                    pos += 1j
                case "S":
                    pos += -1j
                case "E":
                    pos += 1
                case "W":
                    pos += -1

            if pos in visited:
                # print(visited)
                return True
            else:
                visited.add(pos)
        # print(visited)
        return False


s = Solution()
print(s.isPathCrossing("NESWW"))
