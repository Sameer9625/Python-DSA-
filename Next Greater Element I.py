# def nextGreaterElement(nums1, nums2):
#     result = []
    
#     for num in nums1:
#         # Step 1: Find index in nums2
#         index = nums2.index(num)
        
#         # Step 2: Search right side
#         found = -1
#         for i in range(index + 1, len(nums2)):
#             if nums2[i] > num:
#                 found = nums2[i]
#                 break
        
#         result.append(found)
    
#     return result

#optimized approach

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        stack = []
        hm = {}
        
        # Traverse from right to left
        for i in range(len(nums2) - 1, -1, -1):
            data = nums2[i]
            
            # Remove smaller elements
            while stack and stack[-1] <= data:
                stack.pop()
            
            # If stack empty → no greater element
            if not stack:
                hm[data] = -1
            else:
                hm[data] = stack[-1]
            
            stack.append(data)
        
        # Build answer
        ans = []
        for val in nums1:
            ans.append(hm[val])
        
        return ans
    

# def nextGreaterElement(nums1, nums2):
#     stack = []
#     next_greater = {}   # dictionary to store next greater element
    
#     # Step 1: Process nums2
#     for num in nums2:
#         while stack and num > stack[-1]:
#             smaller = stack.pop()
#             next_greater[smaller] = num
#         stack.append(num)
    
#     # Step 2: Build result for nums1
#     result = []
#     for num in nums1:
#         result.append(next_greater.get(num, -1))
    
#     return result