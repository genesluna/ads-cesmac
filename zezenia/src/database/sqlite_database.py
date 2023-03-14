"""
This script defines functions to save Zezenia game data to a SQLite database
using SQLAlchemy and Pandas. Specifically, it includes the following functions:

- save_loot_to_database(dataframe, table_name): saves a Pandas DataFrame of loot 
data to a SQLite database table with the given name.
- save_monsters_to_database(dataframe): saves a Pandas DataFrame of monster data
 to an SQLite database.
- save_loot_pivot_to_database(dataframe, loot_type): saves a pivot table of monster
 loot data to the database for a specific type of loot (e.g. "items", "spells", etc.).

The script also sets up a Sqlite connection to the database and defines the necessary
table structures using SQLAlchemy's Table and Column classes. If the tables already
 exist in the database, the script does not recreate them.
"""

from __future__ import annotations
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
import sqlalchemy

# Set up Sqlite connection
engine = create_engine("sqlite:///src/database/zezenia.db")


def save_loot_to_database(dataframe: pd.DataFrame, table_name: str) -> None:
    """
    Save a Pandas DataFrame of loot data to a SQLite database table with the given name.

    Args:
        dataframe (pd.DataFrame): The Pandas DataFrame to save to the database.
        table_name (str): The name of the database table to save the DataFrame to.

    Returns:
        None: This function does not return anything, it simply saves the DataFrame to the database.
    """

    # Create table if it doesn't exist
    if not sqlalchemy.inspect(engine).has_table(table_name):
        # Create metadata object
        meta = MetaData()

        # Define table structure
        ordinary_loot_table = Table(
            table_name,
            meta,
            Column("id", String, primary_key=True),
            Column("name", String, nullable=False),
        )

        # Create table
        meta.create_all(engine)
    else:
        # If the table already exists, do nothing
        return

    # Save dataframe to database
    dataframe.to_sql(table_name, con=engine, if_exists="append", index=True)


def save_monsters_to_database(dataframe: pd.DataFrame) -> None:
    """
    Saves a dataframe containing monster data to an SQLite database.

    Args:
    - dataframe: pandas.DataFrame object containing monster data

    Returns:
    - None
    """

    # Create table if it doesn't exist
    if not sqlalchemy.inspect(engine).has_table("mosters"):
        # Create metadata object
        meta = MetaData()

        # Define table structure
        ordinary_loot_table = Table(
            "monsters",
            meta,
            Column("id", String, primary_key=True),
            Column("name", String, nullable=False),
            Column("life", Float),
            Column("xp", Float),
            Column("specialty", String),
            Column("hunting_location", String),
            Column("image_url", String),
        )

        # Create table
        meta.create_all(engine)
    else:
        # If the table already exists, do nothing
        return

    # Filter dataframe for the columns we need
    filtered_df = dataframe[["name", "life", "xp", "specialty", "hunting_location", "image_url"]].copy()

    # Save filtered dataframe to database
    filtered_df.to_sql("monsters", con=engine, if_exists="append", index=True)


def save_loot_pivot_to_database(dataframe: pd.DataFrame, loot_type: str) -> None:
    """
    Save a pivot table of monster loot data to the database.

    Args:
        dataframe (pandas.DataFrame): The pivot table of monster loot data to save.
        loot_type (str): The type of loot being saved (e.g. "items", "spells", etc.).

    Returns:
        None
    """

    # Create table if it doesn't exist
    if not sqlalchemy.inspect(engine).has_table(f"monster_{loot_type}"):
        # Define base metadata object
        class Base(DeclarativeBase):
            pass

        # Define table structure
        ordinary_loot_table = Table(
            f"monster_{loot_type}",
            Base.metadata,
            Column("monster_id", String, ForeignKey("monsters.id"), primary_key=True),
            Column(f"{loot_type}_id", String, ForeignKey(f"{loot_type}.id"), primary_key=True),
        )

        # Define parent and child classes to create relationship between tables
        class Parent(Base):
            __tablename__ = "monsters"

            id: Mapped[int] = mapped_column(primary_key=True)
            children: Mapped[list[Child]] = relationship(secondary=loot_type, back_populates="parents")

        class Child(Base):
            __tablename__ = loot_type

            id: Mapped[int] = mapped_column(primary_key=True)
            parents: Mapped[list[Parent]] = relationship(secondary="monsters", back_populates="children")

        # Create table
        Base.metadata.create_all(engine)
    else:
        # If the table already exists, do nothing
        return

    # Save dataframe to database
    dataframe.to_sql(f"monster_{loot_type}", con=engine, if_exists="append", index=False)
