import os

def log(log_string: str):
    if os.getenv("MODE") != "DEBUG":
        return

    print(log_string)