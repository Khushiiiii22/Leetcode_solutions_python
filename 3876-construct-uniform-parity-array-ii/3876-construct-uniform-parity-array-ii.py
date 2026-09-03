class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2:
                min_odd = min(min_odd, x)
            else:
                min_even = min(min_even, x)

        # Try making everything odd
        ok_odd = True

        for x in nums1:
            if x % 2 == 0:
                if min_odd >= x:
                    ok_odd = False
                    break

        if ok_odd:
            return True

        # Try making everything even
        ok_even = True

        for x in nums1:
            if x % 2 == 1:
                if min_odd >= x:
                    ok_even = False
                    break

        return ok_even

        