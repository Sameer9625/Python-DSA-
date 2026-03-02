nums = [-2,1,-3,4,-1,2,1,-5,4]

#brute force
n = len(nums)
max_sum = float('-inf')
for i in range(n):
    total = 0
for j in range(i,n):
    total += nums[j]
    max_sum = max(max_sum, total)
print(max_sum)

#optimal kadane's algorithm
n = len(nums)
max_sum = float('-inf')
total = 0
for i in range(n):
    total += nums[i]
    max_sum = max(max_sum, total)
    if total < 0:
        total = 0
print(max_sum)