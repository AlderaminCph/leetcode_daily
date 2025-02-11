import pytest

from array_string.merge_strings_alternately import Solution


@pytest.mark.parametrize(
    ["word1", "word2", "expected_output"],
    [("abc", "pqr", "apbqcr"), ("ab", "pqrs", "apbqrs"), ("abcd", "pq", "apbqcd")],
)
def test_merge_alternately(word1: str, word2: str, expected_output: str):
    assert Solution().merge_alternately(word1, word2) == expected_output
