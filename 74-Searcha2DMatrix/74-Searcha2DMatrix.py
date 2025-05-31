# Last updated: 5/31/2025, 6:38:09 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        leftColumn = 0
        rightColumn = m - 1
        upRow = 0
        downRow = n - 1

        while upRow <= downRow:
            midRow = (upRow + downRow) // 2
            if target < matrix[midRow][leftColumn]:
                downRow = midRow - 1
            elif target > matrix[midRow][rightColumn]:
                upRow = midRow + 1
            else:
                while leftColumn <= rightColumn:
                    midColumn = (leftColumn+rightColumn) //2
                    if target < matrix[midRow][midColumn]:
                        rightColumn = midColumn -1
                    elif target > matrix[midRow][midColumn]:
                        leftColumn = midColumn + 1
                    else:
                        return True
        return False


