"""
This script prepares monster loot data for further analysis by creating dictionaries and dataframes
representing the loot items and their relationships to the monsters, and then saving the data to
a database for future analysis.

The script contains five functions:

- create_loot_dicts: creates dictionaries for ordinary loot and rare loot
- create_loot_dataframes: creates a pandas dataframe for a given loot dictionary
- create_monster_loot_pivot: creates a pandas dataframe for monster-loot pivot
- prepare_data: prepares the data for further analysis by creating dictionaries and dataframes
- save_to_database: saves the data to a database for future analysis

The prepare_data function takes a pandas DataFrame containing information about monsters and their loot
and returns a tuple containing four pandas DataFrames: ordinary_loot_df, rare_loot_df,
monster_ordinary_loot_pivot_df, and monster_rare_loot_pivot_df. The first two DataFrames contain
information about the individual loot items (name and ID), while the latter two DataFrames represent
the relationships between monsters and the loot items they drop (monster ID and loot item ID).

The save_to_database function takes a pandas DataFrame containing information about monsters and their
loot and saves the data to a specified database for future analysis.

The script supports three types of databases: SQLite, PostgreSQL, and Google BigQuery.
"""

import uuid
import time
from halo import Halo
import pandas as pd
from src.database import sqlite_database
from src.database import postgres_database
from src.database import bigquery_database

# Set the progress spinner
spinner = Halo(spinner="dots")


def create_loot_dicts(df: pd.DataFrame) -> tuple:
    """
    Returns dictionaries for ordinary loot and rare loot.

    Args:
        df (pandas.DataFrame): A dataframe containing the monsters data.

    Returns:
        tuple: A tuple containing two dictionaries, one for ordinary loot and one for rare loot.
    """

    # Create empty lists for ordinary loot and rare loot
    ordinary_loot = []
    rare_loot = []

    # Loop through each row of the dataframe
    for idx in df.index:
        # Add the ordinary loot and rare loot from the current row to their respective lists
        ordinary_loot.extend(df["ordinary_loot"][idx])
        rare_loot.extend(df["rare_loot"][idx])

    # Remove duplicates from the lists
    ordinary_loot = list(dict.fromkeys(ordinary_loot))
    rare_loot = list(dict.fromkeys(rare_loot))

    # Create a dictionary for the ordinary loot, where each key is a unique UUID and each value is an item
    ordinary_loot_dict = {}
    for item in ordinary_loot:
        ordinary_loot_dict[str(uuid.uuid4())] = item

    # Create a dictionary for the rare loot, where each key is a unique UUID and each value is an item
    rare_loot_dict = {}
    for item in rare_loot:
        rare_loot_dict[str(uuid.uuid4())] = item

    # Return a tuple containing the dictionaries for ordinary loot and rare loot
    return ordinary_loot_dict, rare_loot_dict


def create_loot_dataframes(loot_dict: dict) -> pd.DataFrame:
    """
    Returns a pandas dataframe for the given loot dictionary.

    Args:
        loot_dict (dict): A dictionary containing the loot items.

    Returns:
        pandas.DataFrame: A dataframe containing the loot data.
    """

    loot_df = pd.DataFrame(loot_dict.items(), columns=["id", "name"])
    loot_df.set_index("id", inplace=True)
    return loot_df


def create_monster_loot_pivot(df: pd.DataFrame, loot_dict: dict, column_name: str) -> pd.DataFrame:
    """
    Returns a pandas dataframe for monster loot pivot.

    Args:
        df (pandas.DataFrame): A dataframe containing the monsters data.
        loot_dict (dict): A dictionary containing the loot items.
        column_name (str): The name of the column containing the loot items.

    Returns:
        pandas.DataFrame: A dataframe containing the monster-loot pivot data.
    """
    # Loop through the dataframe and create a list of monster-loot pairs.
    monster_loot_pivot = []
    for idx in df.index:
        # For each monster in the dataframe, get its loot items in the specified column.
        for item in df[column_name][idx]:
            # Check which loot item in the dictionary matches the current item from the dataframe.
            loot_id = {i for i in loot_dict if loot_dict[i] == item}
            # Append the monster-loot pair to the list.
            monster_loot_pivot.append([str(idx), list(loot_id)[0]])

    # Convert the list of monster-loot pairs into a pandas dataframe.
    monster_loot_pivot_df = pd.DataFrame(monster_loot_pivot, columns=["monster_id", f"{column_name}_id"])

    # Return the monster-loot pivot dataframe.
    return monster_loot_pivot_df


def prepare_data(monsters_df: pd.DataFrame) -> tuple:
    """
    Given a pandas DataFrame `monsters_df` containing information about monsters
    and their loot, prepares the data for further analysis by creating dictionaries
    and DataFrames representing the loot items and their relationships to the monsters.

    Args:
        monsters_df: A pandas DataFrame containing columns "name", "ordinary_loot",
            and "rare_loot". The "ordinary_loot" and "rare_loot" columns are lists
            of strings representing the names of the loot items that can be obtained
            from each monster.

    Returns:
        A tuple containing four pandas DataFrames: (ordinary_loot_df, rare_loot_df,
        monster_ordinary_loot_pivot_df, monster_rare_loot_pivot_df). The first two
        DataFrames contain information about the individual loot items (name and ID),
        while the latter two DataFrames represent the relationships between monsters
        and the loot items they drop (monster ID and loot item ID).
    """

    ordinary_loot_dict, rare_loot_dict = create_loot_dicts(monsters_df)

    ordinary_loot_df = create_loot_dataframes(ordinary_loot_dict)
    rare_loot_df = create_loot_dataframes(rare_loot_dict)

    monster_ordinary_loot_pivot_df = create_monster_loot_pivot(monsters_df, ordinary_loot_dict, "ordinary_loot")

    monster_rare_loot_pivot_df = create_monster_loot_pivot(monsters_df, rare_loot_dict, "rare_loot")

    return (ordinary_loot_df, rare_loot_df, monster_ordinary_loot_pivot_df, monster_rare_loot_pivot_df)


def save_to_bigquery_database(monsters_df: pd.DataFrame) -> None:
    """
    Given a pandas DataFrame `monsters_df` containing information about monsters
    and their loot, saves the data to a BigQuery table for future analysis.

    Args:
        monsters_df: A pandas DataFrame containing columns "name", "ordinary_loot",
            "rare_loot", etc.

    Returns:
        None.

    Side effects:
        Saves the data to a BigQuery table using the `save_dataframe_to_bigquery()`
        function from the `bigquery_database` module. The table is created in the
        default dataset and project specified in the configuration settings. The
        schema of the table is inferred from the input DataFrame `monsters_df`, and
        the column names are automatically mapped to the corresponding BigQuery
        field names. If the table already exists, the function will append the
        data to the existing table. If the table does not exist, it will be created
        with the appropriate schema.
    """
    # Saves the data do Goolgle BigQuery
    print("\n💾 Saving data to Google BigQuery\n")
    bigquery_database.save_dataframe_to_bigquery(monsters_df)


def save_to_sqlite_database(monsters_df: pd.DataFrame) -> None:
    """
    Given a pandas DataFrame `monsters_df` containing information about monsters
    and their loot, prepares the data and saves it to an SQLite database for future
    analysis.

    Args:
        monsters_df: A pandas DataFrame containing columns "name", "ordinary_loot",
            and "rare_loot". The "ordinary_loot" and "rare_loot" columns are lists
            of strings representing the names of the loot items that can be obtained
            from each monster.

    Returns:
        None.

    Side effects:
        Saves the data to an SQLite database using functions from the `sqlite_database`
        module. Four tables are created: "monsters", "ordinary_loot", "rare_loot", and
        "monster_loot_pivot". The "monsters" table contains the original data from
        `monsters_df`, while the other three tables represent the loot items and their
        relationships to the monsters. The "monster_loot_pivot" table has a foreign key
        reference to both the "monsters" and "loot" tables, and represents the many-to-many
        relationship between monsters and loot items.
    """

    print("\n💾 Saving data to SQlite database\n")
    spinner.start(text="Preparing the data")
    ordinary_loot_df, rare_loot_df, monster_ordinary_loot_pivot_df, monster_rare_loot_pivot_df = prepare_data(
        monsters_df
    )
    spinner.succeed()

    # Save the tables to Sqlite
    spinner.start(text="Saving the monsters")
    sqlite_database.save_monsters_to_database(monsters_df)
    time.sleep(1)
    spinner.succeed()
    spinner.start(text="Saving the ordinary loot")
    sqlite_database.save_loot_to_database(ordinary_loot_df, "ordinary_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Saving the rare loot")
    sqlite_database.save_loot_to_database(rare_loot_df, "rare_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Saving the ordinary loot relationship with monsters")
    sqlite_database.save_loot_pivot_to_database(monster_ordinary_loot_pivot_df, "ordinary_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Saving the rare loot relationship with monsters")
    sqlite_database.save_loot_pivot_to_database(monster_rare_loot_pivot_df, "rare_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Finishing the job")
    time.sleep(0.5)
    spinner.succeed(text="Job done!")


def save_to_postgres_database(monsters_df: pd.DataFrame) -> None:
    """
    Given a pandas DataFrame `monsters_df` containing information about monsters
    and their loot, prepares the data and saves it to an Postgres database for future
    analysis.

    Args:
        monsters_df: A pandas DataFrame containing columns "name", "ordinary_loot",
            and "rare_loot". The "ordinary_loot" and "rare_loot" columns are lists
            of strings representing the names of the loot items that can be obtained
            from each monster.

    Returns:
        None.

    Side effects:
        Saves the data to a Postgres database using functions from the `postgres_database`
        module. Four tables are created: "monsters", "ordinary_loot", "rare_loot", and
        "monster_loot_pivot". The "monsters" table contains the original data from
        `monsters_df`, while the other three tables represent the loot items and their
        relationships to the monsters. The "monster_loot_pivot" table has a foreign key
        reference to both the "monsters" and "loot" tables, and represents the many-to-many
        relationship between monsters and loot items.
    """

    print("\n💾 Saving data to Postgress database\n")
    spinner.start(text="Preparing the data")
    ordinary_loot_df, rare_loot_df, monster_ordinary_loot_pivot_df, monster_rare_loot_pivot_df = prepare_data(
        monsters_df
    )
    time.sleep(0.3)
    spinner.succeed()

    # Save the tables to Sqlite
    spinner.start(text="Saving the monsters")
    postgres_database.save_monsters_to_database(monsters_df)
    time.sleep(1)
    spinner.succeed()
    spinner.start(text="Saving the ordinary loot")
    postgres_database.save_loot_to_database(ordinary_loot_df, "ordinary_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Saving the rare loot")
    postgres_database.save_loot_to_database(rare_loot_df, "rare_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Saving the ordinary loot relationship with monsters")
    postgres_database.save_loot_pivot_to_database(monster_ordinary_loot_pivot_df, "ordinary_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Saving the rare loot relationship with monsters")
    postgres_database.save_loot_pivot_to_database(monster_rare_loot_pivot_df, "rare_loot")
    time.sleep(0.3)
    spinner.succeed()
    spinner.start(text="Finishing the job")
    time.sleep(0.5)
    spinner.succeed(text="Job done!")
