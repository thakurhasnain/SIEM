import json

def correlate_events(normalized_file, incidents_file):
    with open(normalized_file) as infile, open(incidents_file, 'w') as outfile:
        for line in infile:
            log_entry = json.loads(line)
            if detect_incident(log_entry):
                outfile.write(json.dumps(log_entry) + "\n")

def detect_incident(log_entry):
    # Example incident detection logic
    if "error" in log_entry["message"].lower():
        return True
    return False

if __name__ == "__main__":
    normalized_file = "normalized_logs.json"
    incidents_file = "incidents.json"
    correlate_events(normalized_file, incidents_file)
