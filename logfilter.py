import os
import argparse
import sys

def filter_logs(logs, log_type="INFO"):
    filtered_logs = []
    for log in logs:
        space_separated = log.split(" ")
        for element in space_separated:
            if element.startswith(log_type):
                filtered_logs.append(log)
                break

    return filtered_logs


def filter_log_file(source_filename: str, file_type: str, destination_filename: str) -> None:
    with open(os.path.join("data", source_filename), "r") as f:
        logs = [line for line in f]

    # Filter the logs by the relevant type
    filtered_logs = filter_logs(logs, file_type)

    # Save to a new file
    with open(destination_filename + "_" + file_type, "a") as f:
        f.writelines(filtered_logs)

def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Generate a new file containing only logs of a specific severity."
    )
    parser.add_argument("source", help="Name of the source log file (in the data/ folder).")
    parser.add_argument("destination", help="Prefix for the destination file.")
    parser.add_argument(
        "--type",
        default="INFO",
        help="Log type to filter (default: INFO, e.g., ERROR, WARNING)."
    )

    args = parser.parse_args(argv)

    filter_log_file(args.source, args.type, args.destination)


if __name__ == "__main__":
    sys.exit(main())