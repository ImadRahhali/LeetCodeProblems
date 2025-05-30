// Last updated: 5/30/2025, 7:34:38 PM
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int n = nums.length;
        
        // Iterate over each starting point of subarrays
        for (int start = 0; start < n; start++) {
            int currentSum = 0;
            
            // Iterate over each possible end point for the subarray
            for (int end = start; end < n; end++) {
                currentSum += nums[end];  // Accumulate the sum of subarray
                
                // If the sum equals k, increment the count
                if (currentSum == k) {
                    count++;
                }
            }
        }
        
        return count;
    }
}
