class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        sx,sy=source
        tx,ty=target
        if sx==tx and sy==ty:
            return 0
        elif sx==tx or sy==ty or sx+sy==tx+ty or sx-sy==tx-ty:
            return 1
        else:
            return 2
