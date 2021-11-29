def double_zeros(nums, i):
    n = len(nums)
    if i == n:
        return nums
    for j in range(n-2, i-1, -1):
        nums[j+1] = nums[j]
    nums[i] = 0
    
def solve(nums):
    n = len(nums)
    i = 0
    while i < n:
        print(i)
        if nums[i] == 0:
            print('Before ', i, nums)
            double_zeros(nums, i+1)
            i = i + 1
            print('After ', i, nums)
        i = i + 1
    return nums


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 2]
    #solve(nums)
    print(solve(nums))