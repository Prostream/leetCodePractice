#
from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_cabdy = max(candies)
    ans = []
    for c in candies:
        if c + extraCandies >= max_cabdy:
            ans.append(True)
        else:
            ans.append(False)
    return ans

