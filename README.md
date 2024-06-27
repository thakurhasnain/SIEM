# SIEM
Security Information and Event Management

## SIEM Components

The `sims` directory contains various scripts and files for the SIEM system:

- `log_collector.py`: Collects logs from various sources and appends them to `collected_logs.txt`.
- `log_normalizer.py`: Normalizes collected logs and saves them to `normalized_logs.json`.
- `log_storage.py`: Stores normalized logs in `log_storage.json`.
- `alert_generator.py`: Generates alerts from incidents and saves them to `alerts.json`.
- `event_correlator.py`: Correlates events to identify incidents and saves them to `incidents.json`.

### Usage

1. Run the log collector:
    ```bash
    python sims/log_collector.py
    ```

2. Run the log normalizer:
    ```bash
    python sims/log_normalizer.py
    ```

3. Run the log storage:
    ```bash
    python sims/log_storage.py
    ```

4. Run the alert generator:
    ```bash
    python sims/alert_generator.py
    ```

5. Run the event correlator:
    ```bash
    python sims/event_correlator.py
    ```

### Logs and Alerts

- Logs collected are stored in `sims/logs/`.
- Normalized logs are saved in `sims/normalized_logs.json`.
- Alerts are saved in `sims/alerts.json`.
- Incidents are stored in `sims/incidents.json`.
