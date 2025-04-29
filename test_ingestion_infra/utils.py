"""
Utiltiy funcitons for parsing the CIF file, reading the secrets and transforming the dataframes
"""

import json
import logging

import pandas as pd

logging.basicConfig(
    format="%(asctime)s-%(levelname)s - %(module)s - %(funcName)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def parse_li_line(line: str) -> dict[str, str]:
    """
    Parsing LI (intermediate station) values for specific train based on uid and date.

    Args:
        line (str): The line extract from CIF file.

    Returns:
        JSON: Json formatted data with given field_lengths.
    """

    field_lengths = {
        "Record_Identity": 2,
        "Location": 8,
        "Scheduled_Arrival Time": 5,
        "Scheduled_Departure Time": 5,
        "Scheduled_Pass": 5,
        "Public_Arrival": 4,
        "Public_Departure": 4,
        "Platform": 3,
        "Line": 3,
        "Path": 3,
        "Activity": 12,
        "Engineering_Allowance": 2,
        "Pathing_Allowance": 2,
        "Performance_Allowance": 2,
        "Spare": 20,
    }

    # Start index for each field
    start_index = 0
    parsed_data = {}

    # Iterate over each field and extract its value
    for field, length in field_lengths.items():
        value = line[start_index : start_index + length].strip()
        parsed_data[field] = value
        start_index += length

    # Convert parsed data to JSON
    return parsed_data


def to_uppercase(text: str) -> str:
    return text.upper()


def add(a, b):
    return a + b


# TODO: Please update this when you have more information available
def later_updates():
    pass


def capitalize_words(sentence: str) -> str:
    """Capitalizes the first letter of each word in a sentence."""
    return " ".join(word.capitalize() for word in sentence.split())
