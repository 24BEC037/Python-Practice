# Program 13: Convert bytes into KB, MB and GB

def bytes_to_units():
    # Get input from user
    bytes_value = float(input("Enter size in bytes: "))
    
    # Convert bytes to KB (1 KB = 1024 bytes)
    kb = bytes_value / 1024
    
    # Convert KB to MB (1 MB = 1024 KB)
    mb = kb / 1024
    
    # Convert MB to GB (1 GB = 1024 MB)
    gb = mb / 1024
    
    # Display results
    print(f"{bytes_value} byte(s) is equal to:")
    print(f"Kilobytes: {kb} KB")
    print(f"Megabytes: {mb} MB")
    print(f"Gigabytes: {gb} GB")

if __name__ == "__main__":
    bytes_to_units()