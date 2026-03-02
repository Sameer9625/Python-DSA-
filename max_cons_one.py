nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
max_count = 0
count = 0   
for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
print(max(max_count, count))