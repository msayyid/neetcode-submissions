class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # most = 0
        # res = []
        # for i in range(len(people)):
        #     for j in range(len(people)):
        #         if i != j:
        #             cur_most = people[i] + people[j]
        #             if cur_most > most and cur_most <= limit:
        #                 most = cur_most
                        

        l, r = 0, len(people) - 1
        count = 0
        people.sort()
        while l < r:
            if people[l] + people[r] > limit:
                count += 1
                r -= 1
            else:
                count += 1
                l += 1
                r -= 1
        if l == r:
            count += 1
        
        return count