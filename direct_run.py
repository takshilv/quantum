import os
import subprocess
import time
import logging

# Configure logging
logging.basicConfig(
    filename="/home/ubuntu/quantum/quantum/job_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_python_script():
    logging.info("4GB Python script start time: %d" % time.time())

    start_time = time.time()

    # Define the paths
    python_path = "/home/ubuntu/quantum/quantum/myenv/bin/python3"  # Path to Python interpreter
    script_path = "/home/ubuntu/quantum/quantum/qml_integration_development.py"  # Path to the Python script
    log_path = "/home/ubuntu/quantum/quantum/logfile.log"  # Path to log file

    # Construct the command
    command = [python_path, "-u", script_path]

    # Execute the command and redirect output to log file
    logging.info(f"Executing command: {' '.join(command)}")
    try:
        with open(log_path, "a") as log_file:
            subprocess.run(command, stdout=log_file, stderr=log_file, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Python script execution failed: {str(e)}")

    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Job executed in {execution_time:.2f} seconds.")

if __name__ == "__main__":
    run_python_script()
