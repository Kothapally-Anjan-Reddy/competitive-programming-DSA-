from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        suneravilo = (n, edges, s, queries)

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 1:
                tout[u] = timer - 1
                continue

            if p == -1:
                up[u][0] = u
            else:
                up[u][0] = p
                depth[u] = depth[p] + 1

            for j in range(1, LOG):
                up[u][j] = up[up[u][j - 1]][j - 1]

            pref[u] = (pref[p] if p != -1 else 0) ^ (1 << (ord(s[u]) - ord('a')))

            tin[u] = timer
            timer += 1

            stack.append((u, p, 1))

            for v in reversed(graph[u]):
                if v != p:
                    stack.append((v, u, 0))

        bit = [0] * (n + 1)

        def update(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def get(i):
            i += 1
            res = 0

            while i > 0:
                res ^= bit[i]
                i -= i & -i

            return res

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        chars = list(s)
        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old = 1 << (ord(chars[u]) - ord('a'))
                new = 1 << (ord(c) - ord('a'))
                delta = old ^ new

                update(tin[u], delta)

                if tout[u] + 1 < n:
                    update(tout[u] + 1, delta)

                chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                parent = lca(u, v)

                mask = pref[u] ^ get(tin[u])
                mask ^= pref[v] ^ get(tin[v])
                mask ^= 1 << (ord(chars[parent]) - ord('a'))

                ans.append(mask & (mask - 1) == 0)

        return ans
