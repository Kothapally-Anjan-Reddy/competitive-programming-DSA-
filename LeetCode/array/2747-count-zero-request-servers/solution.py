class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda x: x[1])

        q = sorted([(t, i) for i, t in enumerate(queries)])

        requests = defaultdict(int)
        result = [0] * len(queries)

        l = r = 0

        for query, idx in q:

            while r < len(logs) and logs[r][1] <= query:
                requests[logs[r][0]] += 1
                r += 1

            while l < r and logs[l][1] < query-x:
                requests[logs[l][0]] -= 1

                if requests[logs[l][0]] == 0:
                    del requests[logs[l][0]]

                l += 1

            result[idx] = n - len(requests)

        return result
