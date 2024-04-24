class Order:
    def __init__(self, order_id, x, y):
        self.order_id = order_id
        self.x = x
        self.y = y
    
    def __dict__(self):
        return {'order_id': self.order_id, 'x': self.x, 'y': self.y}