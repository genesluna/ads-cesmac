from simple_term_menu import TerminalMenu
from src.models.menu import Menu
from src.models.hall import Hall
from src.models.kitchen import Kitchen
from src.models.order import Order
from src.models.payment import Payment
from src.payment_manager import PaymentManager
from copy import deepcopy
import random
from os import system


class AppMenus:
    def __init__(self) -> None:
        self.hall = Hall()
        self.menu = Menu()
        self.kitchen = Kitchen()
        self.payment_manager = PaymentManager()
        system("clear")

    def main_menu(self):
        options = [
            "Adicionar pedido",
            "Mesas Ativas".ljust(16),
            "Cozinha".ljust(16),
            "Relatórios".ljust(16),
            "",
            "Sair".ljust(16),
        ]
        main_menu = TerminalMenu(options, title="\nMenu principal (Refeitório CESMAC)\n", skip_empty_entries=True)
        main_menu_exit = False

        while not main_menu_exit:
            menu_entry_index = main_menu.show()

            match menu_entry_index:
                case 0:
                    self.__order_menu()
                case 1:
                    self.__active_tables_menu()
                case 2:
                    self.__kitchen_menu()
                case 3:
                    pass
                case 5:
                    main_menu_exit = True

    def __order_menu(self):
        all_tables = self.hall.get_tables_names()
        all_tables.extend(["", "<- Voltar".center(11)])

        tables_menu = TerminalMenu(all_tables, title="\nEscolha a mesa:\n", skip_empty_entries=True)
        add_order_menu_back = False

        while not add_order_menu_back:
            menu_entry_index = tables_menu.show()
            if "<- Voltar" in all_tables[menu_entry_index]:
                add_order_menu_back = True
            else:
                table = self.hall.tables[menu_entry_index]
                order = Order(table.number)
                menu_itens = self.menu.get_items_names()
                menu_itens.extend(["", "Descartar pedido".ljust(20), "Finalizar pedido".ljust(20)])
                order_items_menu = TerminalMenu(menu_itens, title="\nEscolha o prato:\n", skip_empty_entries=True)
                order_done = False
                while not order_done:
                    menu_entry_index = order_items_menu.show()
                    if "Finalizar pedido" in menu_itens[menu_entry_index]:
                        order_done = True
                        add_order_menu_back = True
                        self.kitchen.queue_order(order)
                        table.add_order(order)
                    elif "Descartar pedido" in menu_itens[menu_entry_index]:
                        order_done = True
                        add_order_menu_back = True
                        order.menu_items.clear()
                    else:
                        qtd = int(input("\nDigite a quantidade: "))
                        system("clear")
                        for i in range(0, qtd):
                            order.add_menu_item(self.menu.menu_items[menu_entry_index])

    def __active_tables_menu(self):
        active_tables = self.hall.get_active_tables()
        table_names = []

        for table in active_tables:
            table_names.append(table.name.center(11))

        if len(active_tables) < 1:
            table_names.append("Sem mesas ativas")

        table_names.extend(["", "<- Voltar".center(11)])

        active_tables_menu = TerminalMenu(
            table_names, title="\nEscolha a mesa para mais informações:\n", skip_empty_entries=True
        )
        active_tables_menu_back = False

        while not active_tables_menu_back:
            menu_entry_index = active_tables_menu.show()
            if "<- Voltar" in table_names[menu_entry_index] or "Sem mesas ativas" in table_names[menu_entry_index]:
                active_tables_menu_back = True
            else:
                selectded_table = active_tables[menu_entry_index]
                menu_items = ["Mostrar items pedidos", "Fechar a conta", "", "<- Voltar"]
                active_table_dedails_menu = TerminalMenu(
                    menu_items, title="\nEscolha a opção desejada:\n", skip_empty_entries=True
                )
                active_table_dedails_menu_back = False

                while not active_table_dedails_menu_back:
                    menu_entry_index = active_table_dedails_menu.show()
                    if "<- Voltar" in menu_items[menu_entry_index]:
                        active_table_dedails_menu_back = True
                    else:
                        match menu_entry_index:
                            case 0:
                                self.__active_table_items_menu(selectded_table)
                                active_table_dedails_menu_back = True
                            case 1:
                                self.__process_payment(selectded_table)
                                active_table_dedails_menu_back = True
                                active_tables_menu_back = True

    def __process_payment(self, selectded_table):
        print("\033[32;5m \nPagamento processado. Mesa liberada.\033[0m")
        payment_methods = ["Cartão de crédito", "Cartão de Débito", "Dinheiro", "PIX"]
        payment = Payment(deepcopy(selectded_table), random.choice(payment_methods))
        self.payment_manager.process_payment(payment)

        for order in selectded_table.orders:
            if order.status == "Pendente" or order.status == "Em preparação":
                self.kitchen.cancel_order(order)

        selectded_table.clear()
        input("\nPressione enter para voltar")
        system("clear")

    def __active_table_items_menu(self, selected_table):
        ordered_items = []
        for order in selected_table.orders:
            for item in order.menu_items:
                ordered_items.append(f"{item.name.ljust(20)} - Situação: {order.status}".ljust(46))

        ordered_items.extend(["", "<- Voltar".center(46)])

        ordered_items_menu = TerminalMenu(ordered_items, title="\nItems pedidos na mesa:\n", skip_empty_entries=True)
        ordered_items_menu_back = False

        while not ordered_items_menu_back:
            menu_entry_index = ordered_items_menu.show()
            if "<- Voltar" in ordered_items[menu_entry_index]:
                ordered_items_menu_back = True

    def __kitchen_menu(self):
        menu_items = ["Fila de pedidos".ljust(15), "Fila de items".ljust(15), "", "<- Voltar".ljust(15)]
        kitchen_items_menu = TerminalMenu(menu_items, title="\nEscolha a opção desejada:\n", skip_empty_entries=True)
        kitchen_menu_back = False

        while not kitchen_menu_back:
            menu_entry_index = kitchen_items_menu.show()

            match menu_entry_index:
                case 0:
                    self.__order_queue_menu()
                case 1:
                    self.__order_items_menu()
                case 3:
                    kitchen_menu_back = True

    def __order_queue_menu(self):
        kitchen_queue = self.kitchen.get_queue()
        menu_items = []

        for order in kitchen_queue:
            menu_items.append(
                f"mesa {order.table_number} - Hora do pedido: {order.order_time.strftime('%H:%M')} - Situação: {order.status}"
            )

        if len(menu_items) < 1:
            menu_items.append("Sem pedidos na fila")

        menu_items.extend(["", "<- Voltar"])
        kitchen_queue_items_menu = TerminalMenu(menu_items, title="\nFila de pedidos:\n", skip_empty_entries=True)
        kitchen_queue_menu_back = False

        while not kitchen_queue_menu_back:
            menu_entry_index = kitchen_queue_items_menu.show()
            if "<- Voltar" in menu_items[menu_entry_index] or "Sem pedidos na fila" in menu_items[menu_entry_index]:
                kitchen_queue_menu_back = True
            else:
                selected_order: Order = kitchen_queue[menu_entry_index]
                menu_items = ["Em preparação".ljust(11), "Finalizado".ljust(11), "", "<- Voltar".ljust(11)]
                order_status_menu = TerminalMenu(
                    menu_items, title="\nMudar a situação do pedido:\n", skip_empty_entries=True
                )
                order_status_menu_back = False
                while not order_status_menu_back:
                    menu_entry_index = order_status_menu.show()
                    if "<- Voltar" in menu_items[menu_entry_index]:
                        order_status_menu_back = True
                    elif "Em preparação" in menu_items[menu_entry_index]:
                        selected_order.set_status("Em preparação")
                        order_status_menu_back = True
                        kitchen_queue_menu_back = True
                    else:
                        selected_order.set_status("Finalizado")
                        self.kitchen.dequeue_order(selected_order)
                        order_status_menu_back = True
                        kitchen_queue_menu_back = True

    def __order_items_menu(self):
        kitchen_queue = self.kitchen.get_queue()
        order_menu_items = []

        for order in kitchen_queue:
            for item in order.menu_items:
                order_menu_items.append(
                    f"mesa {order.table_number} - {item.name.ljust(20)} - Situação: {order.status}".ljust(55)
                )

        if len(order_menu_items) < 1:
            order_menu_items.append("Sem items na fila")

        order_menu_items.extend(["", "<- Voltar"])

        order_items_menu = TerminalMenu(
            order_menu_items, title="\nFila de items para preparação:\n", skip_empty_entries=True
        )
        order_items_menu_back = False

        while not order_items_menu_back:
            menu_entry_index = order_items_menu.show()
            if (
                "<- Voltar" in order_menu_items[menu_entry_index]
                or "Sem pedidos na fila" in order_menu_items[menu_entry_index]
            ):
                order_items_menu_back = True
