from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-setuid-sandbox")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Example usage
driver = init_driver()
driver.get("https://www.example.com")
print("************* driver get done ********************")
print(driver.title)
driver.quit()

#     # chrome_options = Options()
        #     # chrome_options.add_argument('--headless=old')
        #     # os.environ["WDM_CACHE_DIR"] = "/home/ubuntu/.wdm_cache"
        #     chrome_options = Options()
        #     chrome_options.add_argument("--no-sandbox")
        #     chrome_options.add_argument("--disable-dev-shm-usage")
        #     chrome_options.add_argument("--headless")  # Optional: use if needed
        #     chrome_options.add_argument("--disable-gpu")
        #     chrome_options.add_argument("--remote-debugging-port=9222")
        #     chrome_options.add_argument('--disable-setuid-sandbox')
        # # os.environ['WDM_LOCAL'] = '/home/ubuntu/chromedriver_cache'
        # # os.environ["WDM_CACHE_DIR"] = "/home/ubuntu/.wdm_cache"
        # custom_cache_path = os.path.expanduser("~/.wdm")
        # os.environ['WDM_LOCAL'] = custom_cache_path
        #
        # # Ensure the directory exists
        # if not os.path.exists(custom_cache_path):
        #     os.makedirs(custom_cache_path)
        #
        # print(f"WebDriverManager cache directory: {custom_cache_path}")
        #
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, options=chrome_options)
        # # driver = webdriver.Chrome(options=chrome_options)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# import os
#
#
# def init_driver():
#     # options = webdriver.FirefoxOptions()
#     # options.add_argument("--headless")
#     # driver = webdriver.Firefox(options=options)
#     chrome_options = Options()
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--headless")  # Optional: use if needed
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--remote-debugging-port=9222")
#
#     # os.environ['WDM_LOCAL'] = '/home/ubuntu/chromedriver_cache'
#     # os.environ["WDM_CACHE_DIR"] = "/home/ubuntu/.wdm_cache"
#     # # Automatically download and use the correct ChromeDriver
#     # service = Service(ChromeDriverManager().install())
#     # driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver
#
# # Example usage
# driver = init_driver()
# driver.get("https://www.example.com")
# print("************* driver get done ********************")
# print(driver.title)
# driver.quit()

# import os
# import subprocess
# import time
# import logging
#
# # Configure logging
# logging.basicConfig(
#     filename="/home/ubuntu/quantum/quantum/job_execution.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
#
# def run_python_script():
#     logging.info("4GB Python script start time: %d" % time.time())
#
#     start_time = time.time()
#
#     # Define the paths
#     python_path = "/home/ubuntu/quantum/quantum/myenv/bin/python3"  # Path to Python interpreter
#     script_path = "/home/ubuntu/quantum/quantum/qml_integration_development.py"  # Path to the Python script
#     log_path = "/home/ubuntu/quantum/quantum/logfile.log"  # Path to log file
#
#     # Construct the command
#     command = [python_path, "-u", script_path]
#
#     # Execute the command and redirect output to log file
#     logging.info(f"Executing command: {' '.join(command)}")
#     try:
#         with open(log_path, "a") as log_file:
#             subprocess.run(command, stdout=log_file, stderr=log_file, check=True)
#     except subprocess.CalledProcessError as e:
#         logging.error(f"Python script execution failed: {str(e)}")
#
#     end_time = time.time()
#     execution_time = end_time - start_time
#     logging.info(f"Job executed in {execution_time:.2f} seconds.")
#
# if __name__ == "__main__":
#     run_python_script()
#
