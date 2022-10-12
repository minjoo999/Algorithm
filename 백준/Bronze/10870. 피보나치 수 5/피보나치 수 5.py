N = int(input())
nums = [0, 1]
for i in range(2, N+2):
    num = nums[i-2] + nums[i-1]
    nums.append(num)

print(nums[-2])