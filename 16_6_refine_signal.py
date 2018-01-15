import sys
import os
import signal
import time

def interrupt_handler(signum, frame):
    print("Na na na, you can't get me")

if __name__ == "__main__":
    print("My pid:", os.getpid())
    signal.signal(signal.SIGINT, interrupt_handler)
    while True:
        time.sleep(1000)
