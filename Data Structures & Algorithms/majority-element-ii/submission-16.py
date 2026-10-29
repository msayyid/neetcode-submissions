class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            # we are now incrementing the val of key(count[n]) by one, 
            # by deafult they are 0 thanks to defaultdict(int)
            # basically we are just populating our count
            count[n] += 1

            # now this means, do nothing (just go and keep iterating without
            # continuing) if the length is 2 or less
            if len(count) <= 2:
                continue
            
            # if the len(count) > 2:
            new_count = defaultdict(int) # this one is needed to store
            # the keys and values, where values after decrementing are still 
            # greater than 0, otherwise we would have to pop our map, 
            # which could break the loop (which is in following lines)

            for n, c in count.items():
                if c > 1: # this here is from the drawing explanation
                          # popping the map if count is zero
                          # meaning if c is bigger than 1, if we decrement
                          # we still have something (1), therefore 
                          # add new values to the new_count if only the 
                          # decremented values are > 0
                    new_count[n] = c - 1 # here we know that c - 1 is gonna 
                                         # be greater than 0 due to 
                                         # checks above
            # now after we have added the two most frequent elements 
            # to the new_count, we assign it to our own count
            count = new_count

            # this for loop does not guarantee the majority elements greater
            # than n//3, but it does guarantee the most frequent 2 elements

        # now we just verify if the values in our count are actually
        # valid > n//3
        res = []
        for n in count: # this is not a On, this is O(2), as we have at most 2 elements
            if nums.count(n) > len(nums) // 3: # in here i didn't understand the nums.count(n), are we checking how many times n appears direactly in the original array? i think it is just better to check if v > n//3 ? (i mean it does still work tho, because count in arrays is On operation, which won't affect our final time complexity)
                res.append(n)
        return res
            