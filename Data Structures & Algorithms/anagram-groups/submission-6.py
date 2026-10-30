class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        count = [0] * 26
        # print(count)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            # if tuple(count) in my_map:
            #     my_map[tuple(count)].append(s)
            # else:
            #     my_map[tuple(count)] = [s]
            my_map[tuple(count)].append(s)

        # print(my_map)
        return list(my_map.values())