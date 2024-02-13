from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = set()
        losses = defaultdict(int)
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1

        all_win = []
        one_lost = []
        for player in players:
            if losses[player] == 0:
                all_win.append(player)
            elif losses[player] == 1:
                one_lost.append(player)

        return [sorted(all_win), sorted(one_lost)]
