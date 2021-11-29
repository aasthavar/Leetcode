def solve():
    heights = [1,1,4,2,1,3]
    expected = heights[:]
    expected.sort()
    cnt = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            cnt += 1
        
    return cnt


if __name__ == "__main__":
    print(solve())
