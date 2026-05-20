data = None

# My implementation here
def process_data(value):
    if value is None:
        return "No data provided"
    else:
        return f"Processing: {value}"

print(process_data(data))
print(process_data("Hello World!"))