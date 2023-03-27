from src.models.order import Order
from typing import List


class Table:
    def __init__(self, name: str, number: int, capacity: int) -> None:
        self.name = name
        self.number = number
        self.capacity = capacity
        self.in_use = False
        self.orders: List[Order] = []

    def add_order(self, order: Order) -> None:
        self.orders.append(order)
        self.in_use = True

    def clear(self):
        self.in_use = False
        self.orders.clear()
