// Last updated: 5/30/2025, 7:35:03 PM
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int top = 0, bot = m - 1; // Adjusted for rows
        while (top <= bot) {
            int mid = (top + bot) / 2;
            if (target > matrix[mid][n - 1]) {
                top = mid + 1;
            } else if (target < matrix[mid][0]) {
                bot = mid - 1;
            } else {
                break;
            }
        }
        if (top > bot) {
            return false;
        }
        int row = (top + bot) / 2;
        int left = 0, right = n - 1; // Renamed L and R for clarity
        while (left <= right) {
            int mid = (left + right) / 2;
            if (target < matrix[row][mid]) {
                right = mid - 1;
            } else if (matrix[row][mid] < target) {
                left = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
