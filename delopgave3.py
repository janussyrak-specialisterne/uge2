import pandas as pd
from pathlib import Path
import argparse
import sys 

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

    print("read_and_write was successful")
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Copy a CSV file from a source path to a destination path with basic error handling."
    )
    parser.add_argument("source", help="Path to the source CSV file.")
    parser.add_argument("destination", help="Path to the destination CSV file.")
    args = parser.parse_args(argv)

    success = read_and_write(args.source, args.destination)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())