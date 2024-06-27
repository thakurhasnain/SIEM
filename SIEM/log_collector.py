import os

def collect_logs(log_directory, output_file):
    with open(output_file, 'a') as outfile:
        for log_file in os.listdir(log_directory):
            if log_file.endswith(".log"):
                with open(os.path.join(log_directory, log_file)) as infile:
                    for line in infile:
                        outfile.write(line)

if __name__ == "__main__":
    log_directory = "logs/"
    output_file = "collected_logs.txt"
    collect_logs(log_directory, output_file)
