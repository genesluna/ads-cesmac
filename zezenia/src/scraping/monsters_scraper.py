"""
This script scrapes information about monsters from a website and creates a pandas DataFrame with the scraped data.
It uses the requests library to send HTTP requests to the website, and the BeautifulSoup library to parse the HTML response.
"""

import requests
import pandas as pd
import uuid
from tqdm import tqdm
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def get_monsters_page() -> BeautifulSoup:
    """
    Sends a GET request to the monsters page and returns a BeautifulSoup
    object representing the HTML content of the response.

    Return:
        A BeautifulSoup object representing the HTML content of the monsters page.
    """

    try:
        monsters_page = requests.get("https://zezeniabrasil.com/monsters/", headers=headers)
        # raise an exception if the status code is not 200
        monsters_page.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting the monsters page: {e}")
        raise e

    return BeautifulSoup(monsters_page.content, "html.parser")


def get_monsters_details_page(details_page_url: str) -> BeautifulSoup:
    """
    Sends a GET request to the monsters details page and returns a BeautifulSoup
    object representing the HTML content of the response.

    Args:
        details_link(str): Link to the monsters detail page

    Return:
        A BeautifulSoup object representing the HTML content of the monsters details page.
    """
    try:
        monsters_details_page = requests.get(details_page_url, headers=headers)
        monsters_details_page.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting the monsters details page: {e}")
        raise e

    return BeautifulSoup(monsters_details_page.content, "html.parser")


def scrape_monsters_details(details_page_url: str) -> tuple:
    """
    Scrapes the monsters details page to get specialty,
    hunting_location, ordinary_loot and rare_loot informations

    Args:
        details_link(str): Link to the monsters detail page
    Returns:
        a tuple (specialty, hunting_location, ordinary_loot, rare_loot)
    """

    monsters_details_soup = get_monsters_details_page(details_page_url)

    details_rows = monsters_details_soup.find_all("td")
    details_loot = monsters_details_soup.select("td div")

    # Extract the monster's specialty from the 'details_rows' list. If the text content of the element at index 5 is 'enndn dndss',
    # set the specialty to 'Nenhuma'. Otherwise, set it to the text content of the element with whitespace removed.
    specialty = (
        "Nenhuma" if details_rows[5].get_text(strip=True) == "enndn dndss" else details_rows[5].get_text(strip=True)
    )

    # Check if the hunting_location is unknown ('-'). If so, set it to 'Desconhecido'. Otherwise, remove any '-'
    # or whitespace characters from the beginning and end of the hunting_location string.
    hunting_location = (
        "Desconhecido" if details_rows[7].get_text(strip=True) == "-" else details_rows[7].get_text(strip=True)
    )
    if hunting_location != "Desconhecido":
        hunting_location = hunting_location.strip("- ")

    # Check if the monster has any ordinary_loot. If it does, split the text by newlines and remove
    # the first item (which is the 'Ordinary loot' label). Otherwise, add the string 'Nenhum' to the ordinary_loot list.
    ordinary_loot = []

    if details_loot[2].get_text(strip=True) != "Nenhum":
        ordinary_loot = details_loot[2].get_text().split("\n", 1)[1].splitlines()
    else:
        ordinary_loot.append("Nenhum")

    # Check if the monster has any rare_loot. If it does, split the text by newlines and remove
    # the first item (which is the 'Rare loot' label). Otherwise, add the string 'Nenhum' to the rare_loot list.
    rare_loot = []

    if details_loot[5].get_text(strip=True) != "Nenhum":
        rare_loot = details_loot[5].get_text().split("\n", 1)[1].splitlines()
    else:
        rare_loot.append("Nenhum")

    return (specialty, hunting_location, ordinary_loot, rare_loot)


def scrape_monsters() -> pd.DataFrame:
    """
    Scrapes the monsters pages to get the mosters list
    :retutn: a dataframe containig the monsters list with details
    """

    monsters_soup = get_monsters_page()

    # Locate the element with tag 'tr' and create a monsters list
    table_rows = tqdm(monsters_soup.find_all("tr"), colour="green")
    monsters = []

    table_rows.write("\n" + "Processing monster".center(26))

    # Loop over each row in the table and extract the monster's name, life, xp, image link, and details link.
    for i, row in enumerate(table_rows):
        name_tds = row.find_all("td", class_="name")
        spans = row.find_all("span")
        link = row.find("a")
        img = row.find("img")

        if i == 1000:
            break

        for name_td in name_tds:
            name = name_td.get_text(strip=True)
            life = spans[0].get_text(strip=True)
            xp = spans[1].get_text(strip=True)
            img_link = img.get("src")
            details_link = link.get("href")

            table_rows.set_description(name.center(26))

            # Call the scrape_monsters_details function to get the monster's specialty, hunting location, ordinary loot, and rare loot.
            specialty, hunting_location, ordinary_loot, rare_loot = scrape_monsters_details(details_link)

            # Append the extracted information to the monsters list.
            monsters.append(
                [
                    str(uuid.uuid4()),
                    name,
                    float(life),
                    float(xp),
                    specialty,
                    hunting_location,
                    ordinary_loot,
                    rare_loot,
                    img_link,
                ]
            )

    # Create a pandas dataframe with the mosters attributes
    monsters_df = pd.DataFrame(
        monsters,
        columns=[
            "id",
            "name",
            "life",
            "xp",
            "specialty",
            "hunting_location",
            "ordinary_loot",
            "rare_loot",
            "image_url",
        ],
    )
    monsters_df.set_index("id", inplace=True)

    return monsters_df
