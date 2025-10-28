import cx_Oracle

conn = cx_Oracle.connect("chrisorigi", "Myles003", "localhost:1539/FREEPDB1")
cur = conn.cursor()

# Grant privileges to role
cur.execute("GRANT SELECT, INSERT ON employees TO read_only_once")

# Grant privileges to user
cur.execute("GRANT UPDATE, DELETE ON employees TO hr_user")

# Optional: revoke privileges
# cur.execute("REVOKE DELETE ON employees FROM hr_user")

conn.commit()
cur.close()
conn.close()

print("Module 02: Object Privileges applied via Python.")
