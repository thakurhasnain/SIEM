import json

def generate_alerts(incidents_file, alerts_file):
    with open(incidents_file) as infile, open(alerts_file, 'w') as outfile:
        for line in infile:
            incident = json.loads(line)
            alert = create_alert(incident)
            outfile.write(json.dumps(alert) + "\n")

def create_alert(incident):
    return {
        "alert_type": "Security Incident",
        "timestamp": incident["timestamp"],
        "details": incident["message"]
    }

if __name__ == "__main__":
    incidents_file = "incidents.json"
    alerts_file = "alerts.json"
    generate_alerts(incidents_file, alerts_file)
