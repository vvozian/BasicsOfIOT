class OrdersQueue:
    def __init__(self):
        self.orders = []
        self.newOrdersRequireAcknowledgement = False

    def add_order(self, order):
        self.orders.append(order)
        self.newOrdersRequireAcknowledgement = True

    def look_at_next_order(self):
        return self.orders[0]
    
    def set_next_order_as_done(self):
        self.orders.pop(0)
        self.newOrdersRequireAcknowledgement = True

    def get_order_count(self):
        return len(self.orders)
    
    def acknwoledge_orders(self):
        self.newOrdersRequireAcknowledgement = False
    
    def acknowledgement_required(self):
        return self.newOrdersRequireAcknowledgement
    
    def get_orders(self):
        return self.orders