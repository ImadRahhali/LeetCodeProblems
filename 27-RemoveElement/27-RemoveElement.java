// Last updated: 5/30/2025, 7:35:17 PM
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // Initialize k to 0
        int[] t = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                t[k] = nums[i];
                k++;
            }
        }
        for (int i = 0; i < k; i++) {
            nums[i] = t[i];
        }
        return k; // Return the updated length
    }
}
