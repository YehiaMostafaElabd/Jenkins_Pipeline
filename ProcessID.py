import subprocess
import sys


def get_pid(executable):
    try:
        # Run the application
        process = subprocess.Popen([executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Get the PID of the process
        pid = process.pid
        return pid

    except Exception as e:
        print(f'Failed to run the process: {e}')
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python PID.py <executable>")
        sys.exit(1)

    executable = sys.argv[1]
    pid = get_pid(executable)
    if pid is not None:
        print(f'Process ID: {pid}')
    else:
        print("Failed to get the process ID.")
