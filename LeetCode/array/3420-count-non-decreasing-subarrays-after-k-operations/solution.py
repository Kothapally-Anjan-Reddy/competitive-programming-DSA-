
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        dq = deque()

        j = n - 1
        cost = 0
        ans = 0

        # Process the array from right to left
        for i in range(n - 1, -1, -1):

            num = nums[i]

            # Remove smaller elements and update their required cost
            while dq and nums[dq[-1]] < num:

                l = dq.pop()

                # Find the right boundary of the affected group
                r = dq[-1] if dq else j + 1

                # Increase the entire group to the new maximum
                cost += (r - l) * (num - nums[l])

            # Insert current index into the deque
            dq.append(i)

            # Shrink the window until operations are within k
            while cost > k:

                # Remove the rightmost element's contribution
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            # All subarrays starting at i and ending <= j are valid
            ans += j - i + 1

        return ans
