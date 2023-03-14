"""
Script for saving monster data to a BigQuery table using the Google Cloud Platform (GCP).
The script connects to GCP, sets the BigQuery credentials, and defines the schema for the table.
It then creates a BigQuery dataset and table (if they don't exist), and saves a Pandas DataFrame
to the table. The script uses the Google Cloud BigQuery Python client library and the Halo library
for displaying a progress spinner during the data upload process.
"""

from google.cloud import bigquery
import google
from halo import Halo
import pandas as pd
import os

# Set google Big Query credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "src/credentials/genesluna-dev-service-account.json"

# Construct a BigQuery client object.
client = bigquery.Client()

# Set the progress spinner
spinner = Halo(spinner="dots")

# Define the schema of the table.
schema = [
    bigquery.SchemaField("Name", "STRING"),
    bigquery.SchemaField("Life", "NUMERIC"),
    bigquery.SchemaField("XP", "NUMERIC"),
    bigquery.SchemaField("Specialty", "STRING"),
    bigquery.SchemaField("Hunting_Location", "STRING"),
    bigquery.SchemaField("Ordinary_Loot", "STRING", mode="REPEATED"),
    bigquery.SchemaField("Rare_Loot", "STRING", mode="REPEATED"),
    bigquery.SchemaField("Image_URL", "STRING"),
]


def create_dataset(dataset_id: str) -> bigquery.Dataset:
    """
    Checks if a BigQuery dataset exists and creates it if it doesn't.

    Args:
        dataset_id (str): The ID of the dataset to create.

    Returns:
        The created dataset.
    """
    try:
        spinner.start(text="Checking if the dataset already exists")
        # Try to get the dataset with the given ID from BigQuery
        dataset = client.get_dataset(dataset_id)
        spinner.succeed(text=f"The dataset {dataset_id} is ready")
    except google.api_core.exceptions.NotFound:
        # If the dataset doesn't exist, create a new dataset with the given ID
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        try:
            spinner.start(text=f"Creating new dataset {dataset_id}")
            dataset = client.create_dataset(dataset)
            spinner.succeed(text=f"Dataset {dataset_id} created")
        except Exception as e:
            # If there was an error creating the dataset, print the error message and raise the exception
            spinner.fail(text=f"Error creating dataset {dataset.dataset_id}")
            print(str(e))
            raise e

    # Return the created dataset
    return dataset


def create_table(dataset_id: str, table_id: str, schema: list) -> bigquery.Table:
    """
    Creates or overwrites a BigQuery table.

    Args:
        dataset_id (str): The ID of the dataset containing the table.
        table_id (str): The ID of the table to create or overwrite.
        schema (list): A list of BigQuery SchemaField objects representing the table schema.

    Returns:
        The created or overwritten table.
    """

    # Create a new BigQuery Table object with the provided dataset and table ID
    table = bigquery.Table(f"{dataset_id}.{table_id}")

    # Set the schema of the table to the provided schema
    table.schema = schema

    try:
        spinner.start(text=f"Creating or overwriting table {table_id}")

        # Create the table in BigQuery, overwriting it if it already exists
        table = client.create_table(table, exists_ok=True)

        spinner.succeed(text=f"Table {table_id} is ready")
    except Exception as e:
        spinner.fail(text=f"Error creating or overwriting table {table_id}")
        print(str(e))
        raise e

    # Return the created or overwritten table
    return table


def save_dataframe_to_bigquery(dataframe: pd.DataFrame) -> None:
    """
    Saves a Pandas DataFrame to a BigQuery table.

    Args:
        dataframe (Pandas DataFrame): The DataFrame to save to BigQuery.
        dataset_id (str): The ID of the dataset containing the table to save the DataFrame to.
        table_id (str): The ID of the table to save the DataFrame to.
    """
    dataset_id = f"{client.project}.zezenia"
    table_id = "monsters"

    # Remode index from dataframe
    dataframe = dataframe.reset_index(drop=True)

    create_dataset(dataset_id)
    create_table(dataset_id, table_id, schema)

    try:
        # Save the dataframe to google Big Query
        spinner.start(text="Saving the monsters to the database")
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
        job = client.load_table_from_dataframe(
            dataframe,
            f"{dataset_id}.{table_id}",
            job_config=job_config,
        )
        job.result()  # Wait for the job to complete.

        spinner.succeed(text=f"Loaded {len(dataframe)} rows into {table_id} table.")
    except Exception as e:
        spinner.fail(text=f"Error saving the data")
        print(str(e))
