import os

TYPE_INDEX = 20

def filter_logs(logs, log_type="INFO"):
    filtered_logs = []
    type_end = TYPE_INDEX + len(log_type)
    for log in logs:
        if log[TYPE_INDEX:type_end] == log_type:
            filtered_logs.append(log)

    return filtered_logs


def generate_logs(source_filename: str, file_type: str, destination_filename: str) -> None:
    with open(os.path.join("data", source_filename), "r") as f:
        logs = [line for line in f]

    # Filter the logs by the relevant type
    filtered_logs = filter_logs(logs, file_type)

    # Save to a new file
    with open(destination_filename + "_" + file_type, "a") as f:
        f.writelines(filtered_logs)

generate_logs("app_log.txt", "ERROR", "log")