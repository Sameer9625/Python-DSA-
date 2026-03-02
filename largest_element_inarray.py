nums = [55,32,-97,99,3,67]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i]) #if nums[i] > largest: largest = nums[i]
print (largest)

nums = [55,32,-97,99,3,67 ]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i] > largest:
        largest = nums[i]
print(largest)

# Method 2
# largest = float('-inf') # -infinity
# n = len(nums)
# for i in range(0,n):
#     largest = max(largest,nums[i]) #if nums[i] > largest: largest = nums[i]
# print (largest)