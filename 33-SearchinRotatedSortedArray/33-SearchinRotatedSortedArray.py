# Last updated: 6/1/2025, 1:35:40 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1      
              
        while L < R:
            mid = (L+R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        pivot = L

        L, R = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[R]:
            L = pivot
        else:
            R = pivot - 1
        
        while L <= R:
            mid = (L+R) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return -1

            
