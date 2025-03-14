"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Example 1:

>>> Solution().asteroidCollision(asteroids = [5,10,-5])
[5, 10]

Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

>>> Solution().asteroidCollision(asteroids = [8,-8])
[]

Explanation: The 8 and -8 collide exploding each other.
Example 3:

>>> Solution().asteroidCollision(asteroids = [10,2,-5])
[10]

Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

>>> Solution().asteroidCollision(asteroids = [-2,-1,1,2])
[-2, -1, 1, 2]

>>> Solution().asteroidCollision(asteroids = [-2,-2,1,-2])
[-2, -2, -2]
"""

import doctest


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                    stack.pop()
                if stack and stack[-1] == -asteroid:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
        return stack


doctest.testmod()
