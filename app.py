import logging
import random
import time

# Define Datadog-compatible logging format (without trace details)
FORMAT = ('%(asctime)s %(levelname)s [%(name)s] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s] '
          '- %(message)s')

logging.basicConfig(format=FORMAT)
log = logging.getLogger("example-logger")
log.setLevel(logging.INFO)

# List of random log messages
LOG_MESSAGES = [
    "Processing request from user.",
    "Data successfully retrieved.",
    "Connection to database established.",
    "Error: Unable to fetch data from API.",
    "Background task completed successfully.",
    "Warning: High memory usage detected.",
    "User logged in successfully.",
    "Debug: Calculating processing time.",
    "Info: Service health is good.",
    "Critical: Service outage detected!"
]

def log_random_message():
    while True:
        message = random.choice(LOG_MESSAGES)
        log.info(message, extra={
            'dd.service': 'python-service',
            'dd.env': 'production',
            'dd.version': '1.0.1'
        })
        time.sleep(10)

if __name__ == "__main__":
    log.info("Starting random log generator...")
    log_random_message()
    