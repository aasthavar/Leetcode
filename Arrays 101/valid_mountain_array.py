def bin_search(nums):
    n = len(nums)
    if n < 3:
        return -1 
    left, right = 0, len(nums)-1
    while left < right:
        #print(left, right)
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
    if left+1 != len(nums) and nums[left] > nums[left+1]:
        return left
    return -1

def solve3():
    #nums = [14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
    #nums = [0, 2, 3, 3, 5, 2, 1, 0]
    nums = [3, 2, 1]
    n = len(nums)
    v =  bin_search(nums)

    if v == -1 or v == 0 or v == n-1:
        return False
    
    for i in range(v):
        if nums[i] >= nums[i+1]:
            return False
        
    for i in range(v, n-1):
        if nums[i] <= nums[i+1]:
            return False
    return True

def solve2():
    #nums = [14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
    #nums = [0, 2, 3, 3, 5, 2, 1, 0]
    nums = [1, 2, 1]
    i, n = 0, len(nums)
    inc, dec = False, False
    if n<3:
        return False

    while(i+1 < n and nums[i] < nums[i+1]):
        inc = True
        i += 1
    
    while(i+1<n and nums[i] > nums[i+1]):
        dec = True
        i += 1
   
    if i==n-1 and inc and dec:
        return True
    return False
        

if __name__ == "__main__":
    print(solve2())