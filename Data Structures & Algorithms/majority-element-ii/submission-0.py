class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mymap = dict()
        for i in range(len(nums)):
            mymap[nums[i]] = mymap.get(nums[i], 0) +1
        
        res = []
        for key, val in mymap.items():
            if val>len(nums)//3:
                res.append(key)

        return res