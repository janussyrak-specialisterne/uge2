import pandas as pd
import os
import pathlib

def read_and_write(source_file: str, destination_file: str) -> bool:
    if not os.path.exists(source_file):
        print("The source file does not exist. Please ensure that the file name is spelt correctly.")
        return False
    else:
        source_file_exists = True

    source_file_extension = pathlib.Path(source_file).suffix
    destination_file_extension = pathlib.Path(destination_file).suffix
    if source_file_extension != destination_file_extension:
        print("The file extensions are not compatible. Please check for potential misspellings.")
        return False

    destination_file_exists = os.path.exists(destination_file)
    if source_file_exists and not destination_file_exists:
        df = pd.read_csv(source_file)

        try:
            df.to_csv(destination_file)
        except FileExistsError:
            print("The destination file already exists.")
            return False

    return True


read_and_write("data\\source_data.csv", "random.csv")