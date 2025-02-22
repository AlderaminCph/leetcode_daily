"""
1431. Kids With the Greatest Number of Candies

There are n kids with candies.
You are given an integer array candies,
where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n,
where result[i] is true if,
after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.



Example 1:

>>> Solution().kidsWithCandies([2,3,5,1,3], 3)
[True, True, True, False, True]

Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:

>>> Solution().kidsWithCandies([4,2,1,1,2], 1)
[True, False, False, False, False]

Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies,
even if a different kid is given the extra candy.

Example 3:

>>> Solution().kidsWithCandies([12,1,12], 10)
[True, False, True]
"""

import doctest
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for kid in candies:
            res = kid + extraCandies >= max(candies)
            output.append(res)
        return output


doctest.testmod()
