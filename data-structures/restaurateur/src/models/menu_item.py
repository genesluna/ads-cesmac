class MenuItem:
    def __init__(self, item_id: int, name: str, description: str, price: float, category: str) -> None:
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
