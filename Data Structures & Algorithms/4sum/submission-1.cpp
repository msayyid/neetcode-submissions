class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> temp;
        vector<vector<int>> res;

        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                for (int c = 0; c < n; c++) {
                    for (int d = 0; d < n; d++) {
                        if (a != b && b != c && a != c && c != d && b != d && a != d) {
                            temp.clear();
                            if (nums[a] + nums[b] + nums[c] + nums[d] == target) {
                                temp.push_back(nums[a]);
                                temp.push_back(nums[b]);
                                temp.push_back(nums[c]);
                                temp.push_back(nums[d]);
                                sort(temp.begin(), temp.end());
                                if (find(res.begin(), res.end(), temp) == res.end()) {
                                    res.push_back(temp);
                                }
                            }
                        }
                    }
                }
            }
        }

        return res;
    }
};