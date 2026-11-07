class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        import heapq

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        res = []

        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                t, w, idx = heapq.heappop(busy)
                heapq.heappush(available, (w, idx))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] == time:
                    t, w, idx = heapq.heappop(busy)
                    heapq.heappush(available, (w, idx))

            w, idx = heapq.heappop(available)

            heapq.heappush(busy, (time + task, w, idx))
            res.append(idx)

        return res
