import sqlite3
from sqlite3 import Error


def open_connection(file_path):
    """Create connection to the database.

    Parameters
    ----------
    file_path : str
        Describing the path to the SQLite file

    Returns
    -------
    connection : sqlite3.object
        sqlit3 connection object
    """

    connection = None
    try:
        connection = sqlite3.connect(file_path)
        print("Connection is successful")
        return connection
    except Error as e:
        print("Connection failed")


def translate_products(data):
    """Extract the product translation

    This function is for creating dictionary of original product name and
    product name in English.

    Argument:
        - Pandas DataFrame of the product_category_name_translation

    Return:
        - Dictionary of original product name and product name in English
    """

    original_product_name = data["product_category_name"]
    product_in_english = data["product_category_name_english"]

    products = dict(zip(original_product_name,  product_in_english))

    for key in products:
        if "_" in products[key]: 
            products[key] = " ".join(products[key].split("_")).capitalize()
        else:
            products[key] = products[key].capitalize()

    return products
