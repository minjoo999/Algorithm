N = int(input())
nums = [1]
for i in range(1, N+1):
    num = nums[i-1]*i
    nums.append(num)

print(nums[-1])