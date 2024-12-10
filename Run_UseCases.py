import subprocess
import json
import sys
import os

def run_go_test(go_file):
    # Run the Go file
    result = subprocess.run(['go', 'run', go_file], capture_output=True, text=True)

    # Capture stdout and return status
    stdout = result.stdout
    status = result.returncode

    # Extract the file name without the extension from the file path
    test_name = os.path.splitext(os.path.basename(go_file))[0]

    # Prepare the JSON data for the new test result
    new_test_result = {
        "test_name": test_name,
        "status": "Passed" if status == 0 else "Failed"
    }

    # Load existing test results if the file exists
    if os.path.exists("test_results.json"):
        with open("test_results.json", "r") as json_file:
            test_results = json.load(json_file)
    else:
        test_results = []

    # Append the new test result
    test_results.append(new_test_result)

    # Write the updated JSON file
    with open("test_results.json", "w") as json_file:
        json.dump(test_results, json_file, indent=4)

    # Print the JSON data (optional)
    print(json.dumps(test_results, indent=4))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_tests.py <path_to_go_file>")
        sys.exit(1)
    
    go_file_path = sys.argv[1]
    run_go_test(go_file_path)
