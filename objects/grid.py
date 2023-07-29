class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[None for _ in range(width)] for _ in range(height)]

    def update_cell(self, position, state):
        x, y = position
        self.cells[y][x] = state

    def render_grid(self):
        for row in self.cells:
            for cell in row:
                print(cell or ".", end="")
            print()
