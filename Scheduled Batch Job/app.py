import schedule
import time

def process_item(item):
    """Simulate processing an item"""
    print(f"Processing item: {item}, Result: {item**2}")

def process_data():
    """Simulate running the batch job on dummy data"""
    print("Running batch job with dummy data...")
    dummy_data = [1, 2, 3, 4, 5]
    for item in dummy_data:
        process_item(item)
        print("Batch job completed.")

# Schedule the job to run every minute (just for testing)
schedule.every(1).minute.do(process_data)

# Keep the script running to wait for the next scheduled job
while True:
    schedule.run_pending()
    time.sleep(1)
