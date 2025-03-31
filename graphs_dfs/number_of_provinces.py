"""
547. Number of Provinces

There are n cities.
Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities
and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if
the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

>>> Solution().findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]])
2

Example 2:
>>> Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
3

"""

import doctest


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited_provinces = [False] * len(isConnected)
        province_counter = 0

        def dfs(province_number: int):
            visited_provinces[province_number] = True

            for j, el in enumerate(isConnected[province_number]):
                if not visited_provinces[j] and el:
                    dfs(j)

        for province in range(len(isConnected)):
            if not visited_provinces[province]:
                province_counter += 1
                dfs(province)
        return province_counter


doctest.testmod()
