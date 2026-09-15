import auth
import inspect
import database
import models
from sqlalchemy import inspect as inspect_db

print("--- DEBUGGING AUTH MODULE ---")
print(f"File location: {auth.__file__}")

print("\n--- SOURCE CODE OF verify_password ---")
print(inspect.getsource(auth.verify_password))

print("\n--- SOURCE CODE OF get_password_hash ---")
print(inspect.getsource(auth.get_password_hash))

print("\n--- TESTING HASHING ---")
try:
    long_pwd = "a" * 80
    print(f"Attempting to hash password of length {len(long_pwd)}...")
    hashed = auth.get_password_hash(long_pwd)
    print(f"Success! Hash: {hashed[:20]}...")
except Exception as e:
    print(f"FAILED: {e}")

print("\n--- CHECKING DB SCHEMA ---")
inspector = inspect_db(database.engine)
for table in inspector.get_table_names():
    print(f"Table: {table}")
    columns = [col['name'] for col in inspector.get_columns(table)]
    print(f"  Columns: {columns}")
    if table == 'users':
        if 'hashed_password' not in columns:
            print("  ALERT: 'hashed_password' column MISSING in users table!")
        if 'role' in columns:
            print("  ALERT: Found unexpected 'role' column (schema mismatch confirmed).")

print("\n--- END DEBUG ---")
