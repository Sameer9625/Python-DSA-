nums = [1,99,101,98,2,5,3,100]
#brute force
n = len(nums)
max_count = 0
for i in range(n):
    num  = nums[i]
    count = 1
    while num + 1 in nums:
        num += 1
        count += 1
    max_count = max(max_count, count)
print(max_count)

#optimal
nums = [1,1,1,2,3,5,98,99,100,101]
nums.sort()
count = 0
last_smaller = float('-inf')
longest = 0
for i in range(0,n):
    num = nums[i]
    if num - 1 == last_smaller:
        count += 1
        last_smaller = num
    elif num != last_smaller:
        count = 1
        last_smaller = num  
    longest = max(longest, count)
print(longest)

#optimal with set   
nums = [1,1,1,2,3,5,98,99,100,101]
num_set = set(nums)
longest = 0
for num in num_set:
    if num - 1 not in num_set:
        count = 1
        while num + count in num_set:
            count += 1
        longest = max(longest, count)
print(longest)