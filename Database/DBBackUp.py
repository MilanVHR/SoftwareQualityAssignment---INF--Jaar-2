import shutil
import sqlite3
import tempfile
import zipfile
import os
from datetime import datetime

def Backup_database():
    os.makedirs("Backups", exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    
    # Create a temporary file for the backup
    with tempfile.NamedTemporaryFile() as tmpfile:
        tmpfile.name = f'db_backup_{timestamp}.sq3'
        backup_db_path = tmpfile.name
    #os.rename(backup_db_path, f"b_backup_{timestamp}.sq3")

    # Make the backup
    with sqlite3.connect("SQAssignmentDB.db") as src, sqlite3.connect(backup_db_path) as dest:
        src.backup(dest)

    # Zip the backup
    zip_filename = f'db_backup_{timestamp}.zip'
    zip_path = os.path.join("Backups", zip_filename)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(backup_db_path, arcname=os.path.basename(backup_db_path))


    return zip_path

def Restore_database(zip_name: str):
    zip_path = os.path.join("Backups", zip_name)
    
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Backup {zip_name} not found")
    
    # Extract zip to temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(tmpdir)
        
        # Find extracted .sq3 file
        extracted_files = [f for f in os.listdir(tmpdir) if f.endswith('.sq3')]
        backup_db = os.path.join(tmpdir, extracted_files[0])
        
        # Replace current database
        shutil.move(backup_db, "SQAssignmentDB.db")