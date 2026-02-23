nums = ["5 1 6  8 2 4 9"]
n = len(nums)
for i in range(n-2,-1,-1):
    for j in range(i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            is_swap = True
print(nums) if is_swap else print("Already sorted")

