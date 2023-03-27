from src.models.menu_item import MenuItem
from datetime import datetime
from typing import List


class Order:
    def __init__(self, table_number: int) -> None:
        self.table_number = table_number
        self.menu_items: List[MenuItem] = []
        self.order_time = datetime.now()
        self.status = "Pendente"

    def add_menu_item(self, menu_item: MenuItem) -> None:
        self.menu_items.append(menu_item)

    def remove_menu_item(self, menu_item: MenuItem) -> None:
        if menu_item in self.menu_items:
            self.menu_items.remove(menu_item)

    def set_status(self, status: str) -> None:
        self.status = status

    def get_status(self) -> str:
        return self.status
