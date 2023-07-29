class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.positions = [(10, 10)]  # Start in the middle of a 20x20 grid
        self.direction = (0, -1)  # Start moving up
 
    def head(self):
        return self.positions[0]
    
    def move(self, width, height):
        head = self.positions[0]
        new_head_position = (head[0] + self.direction[0], head[1] + self.direction[1])

        # Check if the new head position is within the grid
        if 0 <= new_head_position[0] < width and 0 <= new_head_position[1] < height:
            # Move to the new position if it is within the grid
            self.positions.insert(0, new_head_position)
            self.positions.pop()
        else:
            # Handle the situation when the snake moves out of the grid
            pass  # Replace this with whatever you want to do in this situation


    def grow(self):
        head = self.positions[0]
        new_head_position = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.positions.insert(0, new_head_position)

    def check_collision(self, width, height):
        head = self.positions[0]
        # Check for collision with the boundaries
        if head[0] >= width or head[0] < 0 or head[1] >= height or head[1] < 0:
            return True
        return self.positions[0] in self.positions[1:]

    def check_self_collision(self):
        head = self.positions[0]
        # Check for collision with itself
        if head in self.positions[1:]:
            return True
        return False


    def change_direction(self, direction):
       self.direction = direction
