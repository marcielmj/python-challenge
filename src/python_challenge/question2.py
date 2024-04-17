from bisect import bisect


class Orders:
    def combine_orders(self, requests: list[int], n_max: int) -> int:
        """
        Calculates the minimum number of trips to fulfill monetary requests.

        Parameters:
        requests (List[int]): Monetary values requested by each branch.
        n_max (int): Maximum monetary value that can be carried in a trip.

        Returns:
        int: Minimum number of trips needed to fulfill all requests.
        """
        sorted_requests = sorted(requests)
        trips = 0

        while sorted_requests:
            current = sorted_requests.pop()
            target = n_max - current

            index = bisect(sorted_requests, target)
            if index > 0:
                sorted_requests.pop(index - 1)

            trips += 1

        return trips
