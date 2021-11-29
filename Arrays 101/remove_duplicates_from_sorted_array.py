def solve():
    nums = [1, 1, 2]
    for element in nums:
        for i in range(nums.count(element)-1):
            nums.remove(element)
    print(nums, len(nums))

def solve2():
    nums = [1, 1, 2]
    id = 0
    n = len(nums)
    i=0
    if n == 1:
        print(n)

    while (i+1<n) :
        nums[id] = nums[i]
        id += 1
        while(i+1<n and nums[i] == nums[i+1]):
            i += 1
        i += 1
    if n >= 2 and nums[n-1] != nums[n-2]:
        nums[id] = nums[n-1]
        id += 1
    print(id, nums)

def solve3():
    nums = [1, 1, 2]
    n = len(nums)
    if (n==0):
        return 0
    repeating_element = -101
    i = 0
    for element in nums:
        if element != repeating_element:
            repeating_element = element
            nums[i] = element
            i += 1
    return i

if __name__ == "__main__":
    solve3()