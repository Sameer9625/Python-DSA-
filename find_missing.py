nums1 = [9,6,4,2,3,5,7,0,1]
# n = len(nums1)
# for i in range(0,n+1):
#     if i not in nums1:
#         print(i)

# #brute force approach -2 
# n = len(nums1), freq = {}
# for i in range(0,n+1):
#     freq[i] = 0
# for num in nums1:
#     freq[num] += 1
# for k,v in freq.items():
#     if v == 0:
#         print(k)

#optimal
n = len(nums1)
print(n * (n + 1) // 2 - sum(nums1))



