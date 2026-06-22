from pathlib import Path
import pandas as pd


RAW_DATA_DIR = Path("data/raw")


def load_excel(file_path):
    """
    Load an Excel file.
    """

    df = pd.read_excel(file_path, header=1)

    return df


def load_all_files():
    """
    Load all Excel files from raw folder.
    """

    files = RAW_DATA_DIR.glob("*.xlsx")

    dataframes = {}

    for file in files:
        dataframes[file.stem] = load_excel(file)

    return dataframes


if __name__ == "__main__":
    data = load_all_files()

    for name, df in data.items():
        print(f"{name}: {df.shape}")