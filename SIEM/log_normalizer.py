import json

def normalize_logs(log_file, normalized_file):
    with open(log_file) as infile, open(normalized_file, 'w') as outfile:
        for line in infile:
            log_entry = parse_log(line)
            normalized_log = {
                "timestamp": log_entry["timestamp"],
                "source": log_entry["source"],
                "message": log_entry["message"]
            }
            outfile.write(json.dumps(normalized_log) + "\n")

def parse_log(log_line):
    # Example log parser, should be customized based on log format
    parts = log_line.split(" ")
    return {
        "timestamp": parts[0],
        "source": parts[1],
        "message": " ".join(parts[2:])
    }

if __name__ == "__main__":
    log_file = "collected_logs.txt"
    normalized_file = "normalized_logs.json"
    normalize_logs(log_file, normalized_file)
