def binary_search(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if left != len(nums) and nums[left] == target:
        return left
    return -1

def solve():
    nums = [10,2,2,3]
    n, cnt = len(nums), 0
    if nums.count(0) == 2:
        return True
    nums.sort()
    for element in nums:
        if element != 0 and binary_search(nums, 2*element) != -1:
            return True
    return False


if __name__ == "__main__":
    solve()