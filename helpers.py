import os
import shutil
from datetime import datetime


def cleanup_temp_files(temp_dir):
    """Remove all files from the temporary directory"""
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')  # Log actual deletion errors


def log_cleanup_time(log_file):
    """Log the cleanup time to a specified log file"""
    with open(log_file, 'a') as f:
        f.write(f'Cleanup executed at: {datetime.now()}
')


def remove_old_logs(log_dir, days=7):
    """Remove log files older than specified days from log directory"""
    cutoff_time = datetime.now().timestamp() - (days * 86400)
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        try:
            if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff_time:
                os.unlink(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')  # Log actual deletion errors

# Example usages
# cleanup_temp_files('/path/to/temp')
# log_cleanup_time('/path/to/log_file.log')
# remove_old_logs('/path/to/logs')
