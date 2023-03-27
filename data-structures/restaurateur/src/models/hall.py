import json
from src.models.table import Table
from typing import List


class Hall:
    def __init__(self) -> None:
        self.tables: List[Table] = []
        self.load_tables()

    def load_tables(self) -> None:
        with open("src/data/tables_pt_BR.json", "r") as f:
            data = json.load(f)
            for table_data in data["tables"]:
                table = Table(name=table_data["name"], number=table_data["number"], capacity=table_data["capacity"])
                self.tables.append(table)

    def get_tables_names(self) -> List[str]:
        table_names = []
        for table in self.tables:
            table_names.append(table.name.center(11))

        return table_names

    def get_active_tables(self) -> List[Table]:
        active_tables = []
        for table in self.tables:
            if table.in_use:
                active_tables.append(table)

        return active_tables
