import subprocess

def run_batch_job(script_path):
    """Simulate running a Python batch job script"""
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        print(f"Output:\n{result.stdout}")
        print(f"Error (if any):\n{result.stderr}")
    except Exception as e:
        print(f"Error running the batch job: {e}")

# Example usage
run_batch_job('dummy_job.py')  # Replace with the path to the external script
