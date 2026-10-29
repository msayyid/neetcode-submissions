class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        q = deque() # we store the indices of values to ensure window is correct

        left = right = 0

        while right < len(nums):
            # in the q we will store the max element for the current window
            # so we will be popping if the previous elements become useless
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # we append the next element, this is an element that could
            # potentially be the next max for a window
            q.append(nums[right])

            # we also need to make sure our left boundary is moving 
            # and make sure to remove the max elements that are no longer relevant
            # or not in our window
            if left > q[0]: # if left boundary is greater than the index of the first element in the q, we popleft, to make sure, this element does not become max for other windwos, since the first elmeent in the q is the current max 
                q.popleft()
            # now we need to update the result
            # first check if we have the valid window
            if right + 1 >= k:
                output.append(nums[q[0]]) # q[0] has the largest value's index
                left += 1
            right += 1
        
        return output