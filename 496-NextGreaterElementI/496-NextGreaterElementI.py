# Last updated: 6/22/2025, 9:42:21 AM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = {num : idx for idx, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = indexes[val]
                res[idx] = curr
            if curr in indexes:
                stack.append(curr)
        return res


        # for i in range(len(nums2)):
        #     if nums2[i] not in indexes:
        #         continue
        #     for j in range(i+1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = indexes[nums2[i]]
        #             res[idx] = nums2[j]
        #             break
        # return res