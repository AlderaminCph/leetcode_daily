"""
443. String Compression

Given an array of characters chars,
compress it using the following algorithm:

Begin with an empty string s.
For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately,
but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split
into multiple characters in chars.

After you are done modifying the input array,
return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

>>> Solution().compress(["a","a","b","b","c","c","c"])
6

Explanation: The groups are "aa", "bb", and "ccc".
This compresses to "a2b2c3".

Example 2:

>>> Solution().compress(["a"])
1

Explanation: The only group is "a",
which remains uncompressed since it's a single character.

Example 3:

>>> Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
4

Explanation: The groups are "a" and "bbbbbbbbbbbb".
This compresses to "ab12".

"""

import doctest


class Solution:
    def compress(self, chars: list[str]) -> int:
        result_index, i = 0, 0

        while i < len(chars):
            letter = chars[i]
            cnt = 0
            while (i < len(chars)) and (chars[i] == letter):
                cnt += 1
                i += 1
            chars[result_index] = letter
            result_index += 1
            if cnt > 1:
                for num in str(cnt):
                    chars[result_index] = num
                    result_index += 1

        return result_index


doctest.testmod()
