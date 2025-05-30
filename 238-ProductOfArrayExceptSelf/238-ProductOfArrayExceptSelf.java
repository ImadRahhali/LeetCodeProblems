// Last updated: 5/30/2025, 7:34:40 PM
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] pre = new int[n];
        int[] post = new int[n];
        int[] res = new int[n];
        pre[0] = nums[0];
        post[n-1] = nums[n-1];
        for (int i=1; i<nums.length; i++) {
            pre[i] = nums[i] * pre[i-1];
        }
        for (int i=n-2; i>=0; i--) {
            post[i] = nums[i] * post[i+1];
        }
        for (int i=1; i<n-1; i++) {
            res[i] = pre[i-1] * post [i+1];
        }
        res[0] = post[1];
        res[n-1] = pre[n-2];
        return res;
    }
}  
