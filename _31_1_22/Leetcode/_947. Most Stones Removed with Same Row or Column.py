#947. Most Stones Removed with Same Row or Column

class UnionFind:
    def __init__(self, N):
        self.p = [i for i in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


class Solution:
    def removeStones(self, stones) :
        n = len(stones)
        union_find = UnionFind(20000)

        for x, y in stones:
            union_find.union(x, y + 10000)

        return n - len({union_find.find(x) for x, y in stones})

s=Solution()
val=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
res=s.removeStones(val)
print(res)