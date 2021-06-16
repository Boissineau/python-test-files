from grid import CreateGrid
import random

if __name__ == '__main__':
    x = CreateGrid(9, 9)
    nums = list(range(0, (x.rows * x.cols), 1))
    random.shuffle(nums)
    idx = 0
    for i in range(x.rows):
        for j in range(x.cols):
            x.add_number(i, j, nums[idx])
            idx += 1
    print(x.grid)


    


