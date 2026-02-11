def process_item(item):
    """Simulate processing an item (e.g., squaring a number)"""
    try:
        print(f"Processing item: {item}, Result: {item**2}")  # Squaring the item as an example
    except Exception as e:
        print(f"Error processing item {item}: {e}")

def batch_job(items):
    """Process a list of items"""
    for item in items:
        process_item(item)

# Example usage with dummy data (list of numbers)
dummy_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
batch_job(dummy_data)
