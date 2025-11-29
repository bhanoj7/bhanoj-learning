import re 

def extract_timestamps(file_path):
    with open(file_path, "r") as f:
        logs = f.read()

    # Regex pattern: match anything like [2025-08-06 09:15:27]
    pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]"

    matches = re.findall(pattern, logs)
    return matches

def extract_user_ids(file_path):
    with open(file_path, "r") as f:
        logs = f.read()

    # Regex pattern: match user IDs like [USER_ID: 12345]
    pattern = r"user_id=.*"

    matches = re.findall(pattern, logs)
    return matches

def count_error_logs(file_path):
    with open(file_path, "r") as f:
        logs = f.read()

    # Regex pattern: match error logs
    pattern = r"ERROR .*"

    matches = re.findall(pattern, logs)
    return len(matches)

def extract_txn_id(file_path):
    with open(file_path, "r") as f:
        logs = f.read()

    # Regex pattern: match TXN IDs like [TXN_ID: 12345]
    pattern = r"txn_id=[a-z0-9]+"

    matches = re.findall(pattern, logs)
    return matches

def extract_time_only(file_path):
    with open(file_path, "r") as f:
        logs = f.read()

    # Regex pattern: match time only like [09:15:27]
    pattern = r"\d{2}:\d{2}:\d{2}"

    matches = re.findall(pattern, logs)
    return matches

def extract_all_log_levels(file_path):
    with open(file_path, "r") as f:
        logs = f.read()

    # Regex pattern: match all log levels like [INFO], [ERROR], and their content
    pattern = r"(DEBUG|INFO|WARNING|ERROR|CRITICAL) (.*)"

    matches = re.findall(pattern, logs)
    return matches

# Run it
if __name__ == "__main__":
    ts = extract_timestamps("sample_log.txt")
    for t in ts:
        print(t)
    user_ids = extract_user_ids("sample_log.txt")
    print("user_ids:", user_ids)
    for uid in user_ids:
        print(uid)
    error_count = count_error_logs("sample_log.txt")
    print("Number of error logs:", error_count)
    txn_ids = extract_txn_id("sample_log.txt")
    print("TXN IDs:", txn_ids)
    for txn_id in txn_ids:
        print(txn_id)
    time_only = extract_time_only("sample_log.txt")
    print("Time only:", time_only)
    for time in time_only:
        print(time)
    all_log_levels = extract_all_log_levels("sample_log.txt")
    print("All log levels:", all_log_levels)
    for level in all_log_levels:
        print(level)
