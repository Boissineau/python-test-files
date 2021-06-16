class CreateGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.create_grid()

    def create_grid(self):
        for i in range(self.rows):
            tmp = []
            for j in range(self.cols):
                tmp.append(i+j)
            self.grid.append(tmp)

    def add_number(self, row, col, value):
        self.grid[row][col] = value

if __name__ == '__main__':
    x = CreateGrid(3, 3)
    print(x.grid)