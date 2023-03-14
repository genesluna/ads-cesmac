"""
This script scrapes monster data using the `monsters_scraper` module and saves it to a database using the `database` module.
It first displays a menu to allow the user to select the database they would like to save the data to. 
The options are: SQLite, Postgres, Google BigQuery, or all databases.
Once the user makes their selection, the script saves the data to the selected database(s).
The script uses the `TerminalMenu` module to display the menu to the user.
The `main()` function executes these steps and is called when the script is run directly.
"""

from simple_term_menu import TerminalMenu
from src.scraping import monsters_scraper
from src.database import database


def main():
    # Scrape monsters
    monsters_df = monsters_scraper.scrape_monsters()

    # Print a menu showning the possible save to database options
    print("\nIn which database would you like to save the results?\n")
    options = ["SQLlite database", "Postgress database", "Google BigQuery", "In all databases"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You selected: {options[menu_entry_index]}")

    # Save to the database of choiche or to all of them
    match menu_entry_index:
        case 0:
            # Save the tables to Sqlite
            database.save_to_sqlite_database(monsters_df)
        case 1:
            # Save the tables to Postgres
            database.save_to_postgres_database(monsters_df)
        case 2:
            # Save the dataframe to google Big Query
            database.save_to_bigquery_database(monsters_df)
        case 3:
            # Save to all databases
            database.save_to_bigquery_database(monsters_df)
            database.save_to_sqlite_database(monsters_df)
            database.save_to_postgres_database(monsters_df)


if __name__ == "__main__":
    main()
