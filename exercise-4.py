def chunking_by(numbers, chunck):
    result = []  # This will store all the chunks
    # Loop through the list in steps
    for i in range(0, len(numbers), chunck):
        # Take a slice from i to i+ chunk (may be shorter at the end)
        part = numbers[i:i + chunck]
        result.append(part)  # Add the chunk to the result list
    return result  # Return the full list of chunks

# Get valid list of numbers from user
while True:
    user_input = input("Enter numbers separated by commas: ")
    try:
        # Convert input to list of integers
        numbers = [int(n.strip()) for n in user_input.split(",")]
        break
    except ValueError:
        print("nvalid input")

# Get valid chunk size from user
while True:
    try:
        chunk_size = int(input("Enter chunk size: "))
        if chunk_size <= 0:
            print("Chunk size must be a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input")

# Chunk the list
chunks = chunking_by(numbers, chunk_size)

# Print visual output
print("\nOriginal list:")
print(numbers)
print("\nChunk size:")
print(chunk_size)

print("\nChunks:")
for chunk in chunks:
    print(chunk)