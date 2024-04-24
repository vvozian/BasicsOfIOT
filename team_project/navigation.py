from Coordinate import Coordinate

class Navigation:
    coordinate = Coordinate(0, 0)
    heading = 'x'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_delta(self, x, y):
        return {'x': x - self.coordinate.x, 'y': y - self.coordinate.y}
    
    def set_heading_x(self):
        self.heading = 'x'
    
    def set_heading_y(self):
        self.heading = 'y'
    