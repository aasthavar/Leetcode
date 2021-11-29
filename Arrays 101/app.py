def shift_nums1(nums, len, id, val):
    i = len
    while (i>id):
        nums[i] = nums[i-1]
        i -= 1
    
    nums[id] = val

def solve():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3   

    p1 = 0
    p2 = 0
    len_nums1 = m
    while(p2 < n and p1 < m+n):
        print(p1, p2)
        if nums1[p1] < nums2[p2]:
            p1 += 1
        else :
            shift_nums1(nums1, len_nums1, p1, nums2[p2])
            p2 += 1
            p1 += 1
            len_nums1 += 1
    while(p2<n):
        nums1[m+p2] = nums2[p2]
        p2 += 1
    print(nums1)

def solve2():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3  
    i = m-1
    j = n-1
    idx = m+n-1
    while i >= 0 and j>=0:
        if nums1[i]>=nums2[j]:
            nums1[idx]=nums1[i]
            i-=1
        else:
            nums1[idx]=nums2[j]
            j-=1
        idx-=1
    
    while i>=0:
        nums1[idx]=nums1[i]
        idx-=1
        i-=1
    
    while j>=0:
        nums1[idx]=nums2[j]
        j-=1
        idx-=1

if __name__ == "__main__":
    solve2()