"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid,
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain
the same elements in the same order (i.e., an equal array).

Example 1:

>>> Solution().equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])
1

Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:

>>> Solution().equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
3

Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

"""

import doctest


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        cnt = 0
        for row in grid:
            for column in list(map(list, zip(*grid))):
                if row == column:
                    cnt += 1
        return cnt


doctest.testmod()
