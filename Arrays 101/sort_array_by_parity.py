def solve():
    nums = [0, 1, 2, 4]
    n = len(nums)
    even_pointer = 0
    read_pointer  = 0

    while (read_pointer < n):
        if nums[read_pointer] % 2 == 0 :
            temp = nums[even_pointer]
            nums[even_pointer] = nums[read_pointer]
            nums[read_pointer] = temp
            even_pointer += 1
        read_pointer += 1

    
    print(nums)


if __name__ == "__main__":
    print(solve())
