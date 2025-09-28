class Solution:
class
 
Solution
:
    def largestPerimeter(self, nums: List
    
def
 
largestPerimeter
(
self
, 
nums
: List
[int]) -> int:
[
int
]) -> 
int
:
        nums.sort(reverse=True)
        nums.sort(
reverse
=
True
)
        for i in range(len(nums) - 2):
        
for
 i 
in
 
range
(
len
(nums) - 
2
):
            if nums[i+1] + nums[i+2] > nums[i]:
            
if
 nums[i+
1
] + nums[i+
2
] > nums[i]:
                return nums[i+1] + nums[i+2] + 
                
return
 nums[i+
1
] + nums[i+
2
] + 
nums[i]
nums[i]
        return 0
        
return
 
0




            
            