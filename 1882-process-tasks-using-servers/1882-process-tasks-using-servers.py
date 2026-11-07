class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []
        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                available, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))

            # If no server is free, advance time
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    available, weight, index = heapq.heappop(busy)
                    heapq.heappush(free, (weight, index))

            weight, index = heapq.heappop(free)
            ans.append(index)

            heapq.heappush(busy, (time + task, weight, index))

        return ans


        