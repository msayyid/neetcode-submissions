class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int total = 0;
        
        for (int i = 0; i < nums.length; i++) {
            total = 0;
            
            // Checking if the single element itself equals k
            if (nums[i] == k) {
                count++;
            }
            
            total += nums[i];
            
            // Checking all subsequent subarrays starting from i
            for (int j = i + 1; j < nums.length; j++) {
                total += nums[j];
                if (total == k) {
                    count++;
                }
            }
        }
        
        return count;
    }
}