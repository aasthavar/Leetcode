def solve():
    nums = [17,18,5,4,6,1]
    n = len(nums)
    i = n-1
    maxm = nums[i]
    while i>=1:
        if maxm < nums[i]:
            maxm = nums[i]
        nums[i] = maxm
        i -= 1

    # i = 1
    # while i < n:
    #     nums[i-1] = nums[i]
    #     i += 1
    # nums[n-1]  = -1

    nums = nums[1:] + [-1]
    print(nums)

if __name__ == "__main__":
    print(solve())
