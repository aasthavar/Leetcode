def solution():
    nums = [4,3,2,7,8,2,3,1]
    n = len(nums)

    temp = [0] * n
    
    for element in nums:
        temp[element-1] = element
    
    not_in_nums = []
    for i in range(len(temp)):
        if temp[i] == 0:
            not_in_nums.append(i+1)

    return not_in_nums

def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp

def solution2():
    nums = [1, 1]
    n = len(nums)
    # print(nums)
    for i in range(n):
        while nums[i] != i+1:
            swap(nums, i, nums[i]-1)
            if nums[nums[i]-1] == nums[i]:
                break
        
    not_in_nums = []
    for i in range(n):
        if i+1 != nums[i]:
            not_in_nums.append(i+1)

    return not_in_nums

if __name__ == "__main__":
    print(solution2())

