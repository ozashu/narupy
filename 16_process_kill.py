import sys
import os
import signal

if __name__ == "__main__":
    try:
        pid = int(sys.argv[1])
    except (IndexError, ValueError):
        sys.exit("Usage: python program.py pid_of_a_process")
    else:
        os.kill(pid, signal.SIGINT)

