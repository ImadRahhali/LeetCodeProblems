// Last updated: 5/30/2025, 7:35:30 PM
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> table = new HashMap<>();
        int n = nums.length;
        for (int i =0; i<n; i++) {
            int y = target - nums[i];
            if (table.containsKey(y)) {
                return new int[]{i,table.get(y)};
            }
            table.put(nums[i],i);
            
        }

        return new int[]{}; 
    }
}
