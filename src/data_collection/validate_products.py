
import pandas as pd
from brand_config import Brands, Categories

Valid_categories = list(Categories.keys())


def validate_products(df):
    errors = []

    #check columns
    required_columns = [
        "product_id", "brand", "product_name", "category"
    ]

    for column in required_columns:
        if column not in df.columns:
            errors.append(f"Missing column: {column}")

    #stop if required columns are missing
    if errors:
        return errors

    #check missing required values
    for column in required_columns:
        if df[column].isna().any():
            errors.append(f"Missing values found in {column}")

    #check duplicate product IDs
    product_ids = df["product_id"].dropna()

    if product_ids.duplicated().any():
        errors.append("Duplicate product IDs found")

    #check brand names
    invalid_brands = set(df["brand"].dropna()) - set(Brands)

    if invalid_brands:
        errors.append(f"Invalid brands: {invalid_brands}")

    #check product categories
    invalid_categories = set(df["category"].dropna()) - set(Valid_categories)

    if invalid_categories:
        errors.append(f"Invalid categories: {invalid_categories}")

    #checking numerical fields
    for column in ["official_price", "retailer_price", "review_count"]:
        if column in df.columns:
            values = pd.to_numeric(df[column], errors="coerce")

            if (values.dropna() < 0).any():
                errors.append(f"Negative values found in {column}")

    #checking ratings
    if "rating" in df.columns:
        ratings = pd.to_numeric(df["rating"], errors="coerce")

        if ((ratings.dropna() < 0) | (ratings.dropna() > 5)).any():
            errors.append("Rating must be between 0 to 5")

    return errors
