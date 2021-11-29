def solve():
    nums = [0]
    n = len(nums)
    write_pointer = 0
    read_pointer  = 0

    while (read_pointer < n):
        if nums[read_pointer] != 0:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
        read_pointer += 1

    while (write_pointer < n):
        nums[write_pointer] = 0
        write_pointer += 1
    print(nums)

if __name__ == "__main__":
    print(solve())
