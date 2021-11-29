
def solve(nums):
    n = len(nums)
    first = 0
    last = n - 1
    squares = []
    while first <= last:
        if abs(nums[first]) < abs(nums[last]):
            squares.append(nums[last] ** 2)
            last -= 1
        else:
            squares.append(nums[first] ** 2)
            first += 1
    squares.reverse()
    return squares

if __name__ == "__main__":
    nums = [-4,-3,0,3,10]
    #solve(nums)
    print(solve(nums))