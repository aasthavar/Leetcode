def solve(nums):
    n = len(nums)
    temp = 0
    max_consecutive_ones = 0

    for element in nums:
        if element == 0:
            if temp > max_consecutive_ones:
                max_consecutive_ones = temp
            temp = 0
        else:
            temp += 1

    if temp > max_consecutive_ones:
        max_consecutive_ones = temp

    return max_consecutive_ones

if __name__ == "__main__":
    nums = [1,1,0,0,1,0,1,1,1]
    #solve(nums)
    print(solve(nums))