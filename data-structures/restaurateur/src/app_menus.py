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
    """
    The `AppMenus` class provides a command-line interface (CLI) for interacting with the restaurant management system.
    It presents a series of menus that allow users to view and manage tables, orders, and items in the restaurant.
    The class uses the `TerminalMenu` library to display menus and receive user input. The class is responsible for
    managing the main application loop, initializing the restaurant data (tables, orders, and menu items), and delegating
    tasks to the appropriate handlers. It also includes several private methods for displaying sub-menus and handling user input.
    """

    def __init__(self) -> None:
        # Instantiate necessary objects
        self.hall = Hall()
        self.menu = Menu()
        self.kitchen = Kitchen()
        self.payment_manager = PaymentManager()
        system("clear")

    def main_menu(self):
        # Define options for the main menu
        options = [
            "Adicionar pedido",
            "Mesas Ativas".ljust(16),
            "Cozinha".ljust(16),
            "Relatórios".ljust(16),
            "",
            "Sair".ljust(16),
        ]
        # Create the main menu object
        main_menu = TerminalMenu(options, title="\nMenu principal (Refeitório CESMAC)\n", skip_empty_entries=True)
        main_menu_exit = False

        while not main_menu_exit:
            # Display the main menu and get the selected option index
            menu_entry_index = main_menu.show()

            # Choose the action based on the selected option
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
        # Get the names of all tables and add the "back" option
        all_tables = self.hall.get_tables_names()
        all_tables.extend(["", "<- Voltar".center(11)])

        # Create the tables menu object
        tables_menu = TerminalMenu(all_tables, title="\nEscolha a mesa:\n", skip_empty_entries=True)
        add_order_menu_back = False

        while not add_order_menu_back:
            # Display the tables menu and get the selected table index
            menu_entry_index = tables_menu.show()
            if "<- Voltar" in all_tables[menu_entry_index]:
                add_order_menu_back = True
            else:
                # Create an order object for the selected table
                table = self.hall.tables[menu_entry_index]
                order = Order(table.number)

                # Get the names of all menu items and add the "discard" and "finish" options
                menu_itens = self.menu.get_items_names()
                menu_itens.extend(["", "Descartar pedido".ljust(20), "Finalizar pedido".ljust(20)])

                # Create the order items menu object
                order_items_menu = TerminalMenu(menu_itens, title="\nEscolha o prato:\n", skip_empty_entries=True)
                order_done = False

                while not order_done:
                    # Display the order items menu and get the selected item index
                    menu_entry_index = order_items_menu.show()
                    if "Finalizar pedido" in menu_itens[menu_entry_index]:
                        # If the "finish" option was selected, mark the order as done and add it to the table's orders list
                        order_done = True
                        add_order_menu_back = True
                        self.kitchen.queue_order(order)
                        table.add_order(order)
                    elif "Descartar pedido" in menu_itens[menu_entry_index]:
                        # If the "discard" option was selected, clear the order's items list
                        order_done = True
                        add_order_menu_back = True
                        order.menu_items.clear()
                    else:
                        # Get the quantity of the selected menu item and add it to the order
                        qtd = int(input("\nDigite a quantidade: "))
                        system("clear")
                        for i in range(0, qtd):
                            order.add_menu_item(self.menu.menu_items[menu_entry_index])

    def __active_tables_menu(self):
        # Get a list of all active tables and create a list with their names
        active_tables = self.hall.get_active_tables()
        table_names = []

        for table in active_tables:
            table_names.append(table.name.center(11))

        # Add a message for when there are no active tables and the "back" option
        if len(active_tables) < 1:
            table_names.append("Sem mesas ativas")

        table_names.extend(["", "<- Voltar".center(11)])

        # Create the active tables menu object
        active_tables_menu = TerminalMenu(
            table_names, title="\nEscolha a mesa para mais informações:\n", skip_empty_entries=True
        )
        active_tables_menu_back = False

        while not active_tables_menu_back:
            # Display the active tables menu and get the selected table index
            menu_entry_index = active_tables_menu.show()

            if "<- Voltar" in table_names[menu_entry_index] or "Sem mesas ativas" in table_names[menu_entry_index]:
                # If the "back" or "no active tables" options were selected, exit the loop
                active_tables_menu_back = True
            else:
                # If a table was selected, display a details menu with options to show the order items or process payment
                selectded_table = active_tables[menu_entry_index]
                menu_items = ["Mostrar items pedidos", "Fechar a conta", "", "<- Voltar"]
                active_table_dedails_menu = TerminalMenu(
                    menu_items, title="\nEscolha a opção desejada:\n", skip_empty_entries=True
                )
                active_table_dedails_menu_back = False

                while not active_table_dedails_menu_back:
                    # Display the details menu and get the selected option index
                    menu_entry_index = active_table_dedails_menu.show()

                    if "<- Voltar" in menu_items[menu_entry_index]:
                        # If the "back" option was selected, exit the loop
                        active_table_dedails_menu_back = True
                    else:
                        # If an option was selected, execute the corresponding action and exit both loops
                        match menu_entry_index:
                            case 0:
                                self.__active_table_items_menu(selectded_table)
                                active_table_dedails_menu_back = True
                            case 1:
                                self.__process_payment(selectded_table)
                                active_table_dedails_menu_back = True
                                active_tables_menu_back = True

    def __process_payment(self, selectded_table):
        # Print a message indicating that the payment is being processed
        print("\033[32;5m \nPagamento processado. Mesa liberada.\033[0m")

        # Define the available payment methods and create a Payment object
        payment_methods = ["Cartão de crédito", "Cartão de Débito", "Dinheiro", "PIX"]
        payment = Payment(deepcopy(selectded_table), random.choice(payment_methods))

        # Process the payment using the PaymentManager
        self.payment_manager.process_payment(payment)

        # Cancel any orders that are still pending or being prepared
        for order in selectded_table.orders:
            if order.status == "Pendente" or order.status == "Em preparação":
                self.kitchen.cancel_order(order)

        # Clear the table and wait for the user to press enter
        selectded_table.clear()
        input("\nPressione enter para voltar")
        system("clear")

    def __active_table_items_menu(self, selected_table):
        # Create a list of ordered items for the selected table, displaying their name and status
        ordered_items = []
        for order in selected_table.orders:
            for item in order.menu_items:
                ordered_items.append(f"{item.name.ljust(20)} - Situação: {order.status}".ljust(46))

        # Add a blank line and a "back" option to the end of the list
        ordered_items.extend(["", "<- Voltar".center(46)])

        # Create a menu from the ordered_items list, with a title and skip_empty_entries set to True
        ordered_items_menu = TerminalMenu(ordered_items, title="\nItems pedidos na mesa:\n", skip_empty_entries=True)
        ordered_items_menu_back = False

        while not ordered_items_menu_back:
            # Show the menu and continue to loop until the user chooses the "back" option
            menu_entry_index = ordered_items_menu.show()
            if "<- Voltar" in ordered_items[menu_entry_index]:
                ordered_items_menu_back = True

    def __kitchen_menu(self):
        # Create a list of menu items to be displayed in the TerminalMenu
        menu_items = ["Fila de pedidos".ljust(15), "Fila de items".ljust(15), "", "<- Voltar".ljust(15)]
        # Create a new TerminalMenu with the menu items
        kitchen_items_menu = TerminalMenu(menu_items, title="\nEscolha a opção desejada:\n", skip_empty_entries=True)
        # Create a variable to keep track of whether the user wants to go back to the previous menu
        kitchen_menu_back = False

        # Display the kitchen menu until the user wants to go back to the previous menu
        while not kitchen_menu_back:
            # Show the TerminalMenu and get the index of the selected menu item
            menu_entry_index = kitchen_items_menu.show()

            # Use a match statement to handle the selected menu item
            match menu_entry_index:
                # If "Fila de pedidos" is selected, show the order queue menu
                case 0:
                    self.__order_queue_menu()
                # If "Fila de items" is selected, show the order items menu
                case 1:
                    self.__order_items_menu()
                # If "<- Voltar" is selected, set kitchen_menu_back to True to exit the loop and go back to the previous menu
                case 3:
                    kitchen_menu_back = True

    def __order_queue_menu(self):
        # Get the kitchen queue
        kitchen_queue = self.kitchen.get_queue()
        # Create a list of menu items
        menu_items = []

        # Loop through the kitchen queue and append the order details to the menu_items list
        for order in kitchen_queue:
            menu_items.append(
                f"mesa {order.table_number} - Hora do pedido: {order.order_time.strftime('%H:%M')} - Situação: {order.status}"
            )

        # If there are no items in the kitchen queue, add a message to the menu_items list
        if len(menu_items) < 1:
            menu_items.append("Sem pedidos na fila")

        # Add a "Voltar" option to the menu_items list
        menu_items.extend(["", "<- Voltar"])

        # Create a TerminalMenu object with the menu_items list as options and a title
        kitchen_queue_items_menu = TerminalMenu(menu_items, title="\nFila de pedidos:\n", skip_empty_entries=True)

        # Set a flag for exiting the loop
        kitchen_queue_menu_back = False

        # Loop through the menu until the user selects the "Voltar" option or the "Sem pedidos na fila" message is displayed
        while not kitchen_queue_menu_back:
            # Show the menu and get the selected index
            menu_entry_index = kitchen_queue_items_menu.show()

            # If the user selects the "Voltar" option or the "Sem pedidos na fila" message is displayed, exit the loop
            if "<- Voltar" in menu_items[menu_entry_index] or "Sem pedidos na fila" in menu_items[menu_entry_index]:
                kitchen_queue_menu_back = True
            else:
                # Get the selected order
                selected_order: Order = kitchen_queue[menu_entry_index]

                # Create a menu for changing the status of the selected order
                menu_items = ["Em preparação".ljust(11), "Finalizado".ljust(11), "", "<- Voltar".ljust(11)]
                order_status_menu = TerminalMenu(
                    menu_items, title="\nMudar a situação do pedido:\n", skip_empty_entries=True
                )
                order_status_menu_back = False

                # Loop through the menu for changing the status of the selected order until the user selects the "Voltar" option
                while not order_status_menu_back:
                    menu_entry_index = order_status_menu.show()

                    # If the user selects the "Voltar" option, exit the loop
                    if "<- Voltar" in menu_items[menu_entry_index]:
                        order_status_menu_back = True

                    # If the user selects "Em preparação", set the status of the selected order to "Em preparação" and exit the loop
                    elif "Em preparação" in menu_items[menu_entry_index]:
                        selected_order.set_status("Em preparação")
                        order_status_menu_back = True
                        kitchen_queue_menu_back = True
                    else:
                        # If the user selects "Finalizado", set the status of the selected order to "Finalizado",
                        # dequeue the order from the kitchen queue, and exit the loop
                        selected_order.set_status("Finalizado")
                        self.kitchen.dequeue_order(selected_order)
                        order_status_menu_back = True
                        kitchen_queue_menu_back = True

    def __order_items_menu(self):
        # Get all orders from the kitchen queue
        kitchen_queue = self.kitchen.get_queue()
        # Create an empty list to store menu items
        order_menu_items = []

        # Loop through each order in the kitchen queue
        for order in kitchen_queue:
            # Loop through each menu item in the order
            for item in order.menu_items:
                # Add a formatted string to the menu items list
                order_menu_items.append(
                    f"mesa {order.table_number} - {item.name.ljust(20)} - Situação: {order.status}".ljust(55)
                )

        # If there are no items in the list, add a "no items" message
        if len(order_menu_items) < 1:
            order_menu_items.append("Sem items na fila")

        # Add a "back" option to the menu items list
        order_menu_items.extend(["", "<- Voltar"])

        # Create a new TerminalMenu with the menu items list and a title
        order_items_menu = TerminalMenu(
            order_menu_items, title="\nFila de items para preparação:\n", skip_empty_entries=True
        )

        # Set a variable to keep track of whether the user has chosen to go back
        order_items_menu_back = False

        # Loop until the user chooses to go back
        while not order_items_menu_back:
            # Show the menu and get the user's selection
            menu_entry_index = order_items_menu.show()

            # If the user selects the "back" option or the "no items" option, go back
            if (
                "<- Voltar" in order_menu_items[menu_entry_index]
                or "Sem pedidos na fila" in order_menu_items[menu_entry_index]
            ):
                order_items_menu_back = True
