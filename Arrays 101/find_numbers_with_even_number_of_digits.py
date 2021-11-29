def digits(a):
    num_digits = 0
    while a != 0: 
        a = int(a/10)
        num_digits += 1
    return num_digits

def solve(nums):
    n = len(nums)
    num_even = 0
    for element in nums:
        num_digits = digits(element)
        if num_digits % 2 == 0:
            num_even += 1
    return num_even
if __name__ == "__main__":
    nums = [2, 22, 3, 44]
    #solve(nums)
    print(solve(nums))