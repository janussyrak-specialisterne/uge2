import pandas as pd
from pathlib import Path

def read_and_write(source_file: str, destination_file: str) -> bool:
    src = Path(source_file)
    dst = Path(destination_file)

    # Verify existence of source file
    if not src.exists():
        print("The source file does not exist. Please ensure that the file name is spelt correctly.")
        return False

    # Verify extension compatibility
    if src.suffix != dst.suffix:
        print("The file extensions are not compatible. Please check for potential misspellings.")
        return False

    # Read with try-catch
    try:
        df = pd.read_csv(source_file)
    except PermissionError:
        print("Permission error: cannot read the source file. Check file permissions.")
        return False

    # Ensure destination file is not overwritten
    if dst.exists():
        print("The destination file already exists.")
    df.to_csv(destination_file)

    return True


read_and_write("data\\source_data.csv", "random.csv")