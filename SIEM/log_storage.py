import json

def store_logs(normalized_file, storage_file):
    with open(normalized_file) as infile, open(storage_file, 'a') as outfile:
        for line in infile:
            log_entry = json.loads(line)
            outfile.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    normalized_file = "normalized_logs.json"
    storage_file = "log_storage.json"
    store_logs(normalized_file, storage_file)
