import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def clean_data():

    # Load raw JSON
    df = pd.read_json("data/raw_products.json")

    print("\nRAW DATA:")
    print(df.head())

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # -----------------------------
    # CLEAN PRICE
    # -----------------------------
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # -----------------------------
    # CLEAN REVIEWS
    # -----------------------------
    df["reviews"] = (
        df["reviews"]
        .astype(str)
        .str.replace(" reviews", "", regex=False)
        .str.replace(" review", "", regex=False)
    )

    df["reviews"] = pd.to_numeric(df["reviews"], errors="coerce")

    # -----------------------------
    # HANDLE MISSING VALUES
    # -----------------------------
    df["title"] = df["title"].fillna("Unknown Product")

    df["description"] = df["description"].fillna("No Description")

    df["price"] = df["price"].fillna(0)

    df["reviews"] = df["reviews"].fillna(0)

    df["rating"] = df["rating"].fillna(0)

    # Convert numeric columns
    df["reviews"] = df["reviews"].astype(int)

    df["rating"] = df["rating"].astype(int)

    # -----------------------------
    # SAVE CLEANED DATA
    # -----------------------------
    df.to_csv("data/cleaned_products.csv", index=False)

    logging.info("Cleaned data saved successfully!")

    print("\nCLEANED DATA:")
    print(df.head())

    return df


if __name__ == "__main__":
    clean_data()