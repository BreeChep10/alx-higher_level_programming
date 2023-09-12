import sys

"""
Initialize dictionaries to store file sizes and status code counts
"""


file_sizes = {}
status_code_counts = {}

"""
Initialize variables to keep track of total file size and line count
"""
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        """
        Check if the line has the expected format
        """
        if len(parts) >= 9:
            status_code = parts[-2]
            size = parts[-1]
            
            """
            Update total file size
            """
            total_size += int(size)
            
            """
            Update file size dictionary
            """
            file_sizes[line_count] = total_size
            
            """
            Update status code counts dictionary
            """
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
            
            """
            Print statistics every 10 lines
            """
            if line_count % 10 == 0:
                print("Total file size:", total_size)
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    """
    Handle KeyboardInterrupt (CTRL + C)
    """
    print("Total file size:", total_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

