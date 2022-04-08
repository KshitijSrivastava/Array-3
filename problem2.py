
## Problem2 H-Index (https://leetcode.com/problems/h-index/)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for idx, c in enumerate(citations):
            if n - idx <= c:
                return n - idx
        return 0