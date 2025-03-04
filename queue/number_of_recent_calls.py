"""
933. Number of Recent Calls

You have a RecentCounter class which counts
the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t,
where t represents some time in milliseconds,
and returns the number of requests that has happened in the past 3000 milliseconds
(including the new request).
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

>>> recentCounter = RecentCounter()
>>> recentCounter.ping(1)
1

>>> recentCounter.ping(100)
2

>>> recentCounter.ping(3001)
3

>>> recentCounter.ping(3002)
3

"""

import doctest


class RecentCounter:
    def __init__(self):
        self.request_counter = []

    def ping(self, t: int) -> int:
        self.request_counter.append(t)

        while self.request_counter[0] < t - 3000:
            self.request_counter.pop(0)
        return len(self.request_counter)


doctest.testmod()
