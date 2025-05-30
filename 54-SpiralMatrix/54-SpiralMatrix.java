// Last updated: 5/30/2025, 7:35:05 PM
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        // Initialize result list to store the spiral order
        List<Integer> result = new ArrayList<>();
        
        // Get the number of rows and columns
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        // Define the boundaries for traversal
        int top = 0;         // Starting row
        int left = 0;        // Starting column
        int bottom = rows - 1; // Ending row
        int right = cols - 1;  // Ending column
        
        // Total number of elements in the matrix
        int totalElements = rows * cols;
        
        // Keep track of the number of elements added to the result
        int count = 0;
        
        // Traverse the matrix in a spiral order until we've added all elements
        while (count < totalElements) {
            // Traverse from left to right along the top row
            for (int i = left; i <= right && count < totalElements; i++) {
                result.add(matrix[top][i]);
                count++;
            }
            top++; // Move down to the next row
            
            // Traverse from top to bottom along the right column
            for (int i = top; i <= bottom && count < totalElements; i++) {
                result.add(matrix[i][right]);
                count++;
            }
            right--; // Move left to the next column
            
            // Traverse from right to left along the bottom row
            for (int i = right; i >= left && count < totalElements; i--) {
                result.add(matrix[bottom][i]);
                count++;
            }
            bottom--; // Move up to the next row
            
            // Traverse from bottom to top along the left column
            for (int i = bottom; i >= top && count < totalElements; i--) {
                result.add(matrix[i][left]);
                count++;
            }
            left++; // Move right to the next column
        }
        
        return result; // Return the result list containing the spiral order
    }
}
