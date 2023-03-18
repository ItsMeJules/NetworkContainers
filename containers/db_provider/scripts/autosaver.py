import time
import threading

from constants import *


def write_to_mongo():
    while True:
        time.sleep(AUTOSAVE_INTERVAL_SECONDS)
        if not mutex.locked():
            print("autosaving...")
            print("autosave complete.")


def init_autosave():
    repeating_thread = threading.Thread(target=write_to_mongo)
    repeating_thread.daemon = True

    return repeating_thread
