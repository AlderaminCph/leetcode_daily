"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being
repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

>>> Solution().decodeString(s = "3[a]2[bc]")
'aaabcbc'

Example 2:
>>> Solution().decodeString(s = "3[a2[c]]")
'accaccacc'

Example 3:
>>> Solution().decodeString(s = "2[abc]3[cd]ef")
'abcabccdcdcdef'

"""

import doctest


class Solution:
    def decodeString(self, s: str) -> str:
        stack_numbers, stack_letters = [], []
        result_string = ""
        number = 0
        for symbol in s:
            if symbol.isdigit():
                number = number * 10 + int(symbol)  # in case of multy-digit number
            elif symbol == "[":
                stack_numbers.append(number)
                stack_letters.append(result_string)
                number, result_string = 0, ""
            elif symbol == "]":
                result_string = stack_letters.pop() + result_string * stack_numbers.pop()
            else:
                result_string += symbol
        return result_string


doctest.testmod()
