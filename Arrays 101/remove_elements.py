def solve():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    i = 0
    n = len(nums)
    id = 0
    while(i < n):
        if nums[i] != val :
            nums[id] = nums[i]
            id += 1
        i += 1
    print(nums)

def solve2():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    for i in range(nums.count(val)):
        nums.remove(val)
    print(nums, len(nums))

if __name__ == "__main__":
    solve2()