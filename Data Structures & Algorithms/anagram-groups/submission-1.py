class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force approach
        anagram_list = []
        final_list = []
        my_map = dict()
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            # my_map[key] = [strs[i]]
            if key in my_map:
                my_map[key].append(strs[i])
            else:
                my_map[key] = [strs[i]]
    
            
        return list(my_map.values())