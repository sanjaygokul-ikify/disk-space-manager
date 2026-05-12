    import os
    import numpy as np
    import pandas as pd

    class DiskSpaceManager:
        def __init__(self):
            self.disk_usage = {}

        def analyze(self):
            # Analyze disk space usage
            for root, dirs, files in os.walk('/'):  # Example: replace with actual disk path
                for file in files:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    self.disk_usage[file_path] = file_size

            # Print disk usage
            print('Disk Usage:')
            for file, size in self.disk_usage.items():
                print(f'{file}: {size} bytes')

        def cleanup(self):
            # Cleanup disk space
            for file, size in self.disk_usage.items():
                if size > 1000000:  # Example: remove files larger than 1MB
                    os.remove(file)
                    print(f'Removed {file}')
