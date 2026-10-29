class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)): # we start from len(s1) because we already have the fist window (confirm please)
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a") # we have the current index to add
            count2[index] += 1 # add the current freq of an element in a window to the count2 (i need you help me word this better)
            if count1[index] == count2[index]: # if now they are equal (after we have incremented our count2, our window)
                matches += 1
            elif count1[index] + 1 == count2[index]: # if they were equal before and we broke it now
                matches -= 1
            # just a one more line fo code to confirm 
            # if it was like this:
            # elif count1[index] == count2[index] - 1:
            #     matches -= 1  # question : would this work as well?


            index = ord(s2[l]) - ord("a")
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1 # same question goes in here too, would it work if we did count1[index] == count2[index] + 1?
            l += 1

        return matches == 26
        