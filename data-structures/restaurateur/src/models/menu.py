import json
from src.models.menu_item import MenuItem
from typing import List


class Menu:
    def __init__(self) -> None:
        self.menu_items: List[MenuItem] = []
        self.load_menu_items()

    def load_menu_items(self) -> None:
        with open("src/data/menu_items_pt_BR.json", "r") as f:
            data = json.load(f)
            for item_data in data["menu_items"]:
                menu_item = MenuItem(
                    item_id=item_data["item_id"],
                    name=item_data["name"],
                    description=item_data["description"],
                    price=item_data["price"],
                    category=item_data["category"],
                )
                self.menu_items.append(menu_item)

    def get_items_names(self) -> List[str]:
        items_names = []
        for item in self.menu_items:
            items_names.append(item.name.ljust(20))

        return items_names
