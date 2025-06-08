import sqlite3
import zipfile
import os
import time
from datetime import datetime

def Backup_database():
    # Create a folder where the backups are stoed if it does not exsist
    os.makedirs("Backups", exist_ok=True)

    # Create a backup filename
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_db_filename = f'db_backup_{timestamp}.sq3'
    backup_db_path = os.path.join("Backups", backup_db_filename)

    # Make the backup
    with sqlite3.connect("SQAssignmentDB.db") as src, sqlite3.connect(backup_db_path) as dest:
        src.backup(dest)

    # Zip the backup
    zip_filename = f'db_backup_{timestamp}.zip'
    zip_path = os.path.join("Backups", zip_filename)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(backup_db_path, arcname=backup_db_filename)

    # This refuses to work, because the program its self locks the coppied .sq3 file.
    # os.remove(backup_db_path)

    return zip_path