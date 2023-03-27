from src.models.order import Order
from typing import List


class Kitchen:
    def __init__(self) -> None:
        self.order_queue: List[Order] = []

    def queue_order(self, order: Order) -> None:
        self.order_queue.append(order)

    def dequeue_order(self) -> Order | None:
        if len(self.order_queue) > 0:
            order = self.order_queue.pop(0)
            order.set_status("Ready")
            return order
        else:
            return None

    def dequeue_order(self, order: Order) -> Order | None:
        if len(self.order_queue) > 0:
            order_index = self.order_queue.index(order)
            order = self.order_queue.pop(order_index)
            order.set_status("Finalizado")
            return order
        else:
            return None

    def cancel_order(self, order: Order) -> Order | None:
        if len(self.order_queue) > 0:
            order_index = self.order_queue.index(order)
            order = self.order_queue.pop(order_index)
            order.set_status("Canceled")
            return order
        else:
            return None

    def get_queue_list(self) -> List[dict]:
        queue = []
        for order in self.order_queue:
            for item in order.menu_items:
                queue.append({"table": f"mesa {order.table_number}", "item": item.name})

        return queue

    def get_queue(self) -> List[Order]:
        return self.order_queue.copy()
