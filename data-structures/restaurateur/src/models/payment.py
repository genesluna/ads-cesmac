import uuid
from datetime import datetime
from src.models.table import Table


class Payment:
    def __init__(self, table: Table, payment_method: str) -> None:
        self.payment_id = uuid.uuid4()
        self.table = table
        self.payment_time = datetime.now()
        self.amount_due = self.calculate_amount_due()
        self.payment_method = payment_method

    def calculate_amount_due(self) -> float:
        subtotal = 0
        for order in self.table.orders:
            for menu_item in order.menu_items:
                item_price = menu_item.price
                subtotal += item_price

        service_charge = subtotal * 0.1
        total = subtotal + service_charge
        return total
