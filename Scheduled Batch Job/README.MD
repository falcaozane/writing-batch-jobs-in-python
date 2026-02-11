Scheduled Batch Job with Dummy Data

To run a batch job periodically, you can use the schedule library to automate it.

Explanation:

schedule.every().day.at("02:00").do(process_files): Schedules the process_files() function to run every day at 2 AM.

while True loop: Keeps the script running, checking for pending tasks.

This allows you to automate batch processing without having to manually execute the job every time.

What It Does:

The process_data() function runs every minute, simulating a batch job that processes a list of numbers.

How to Run:

Install the schedule library with pip install schedule.

Run the script, and it will print the result of processing each number every minute.