import cx_Oracle

conn = cx_Oracle.connect("system", "oracle", "localhost/XEPDB1")
cur = conn.cursor()

# Create roles
for role in ["admin_role", "dev_role", "read_only_role"]:
    try:
        cur.execute(f"CREATE ROLE {role}")
    except cx_Oracle.DatabaseError as e:
        print(f"Role {role} might already exist: {e}")

# Grant object privileges
cur.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON employees TO dev_role")
cur.execute("GRANT SELECT ON employees TO read_only_role")

# Grant system privileges to admin
cur.execute("GRANT CREATE USER, ALTER USER, DROP USER TO admin_role")

# Assign roles to users
cur.execute("GRANT admin_role TO system_admin")
cur.execute("GRANT dev_role TO hr_user")
cur.execute("GRANT read_only_role TO analyst_user")

conn.commit()
cur.close()
conn.close()

print("Module 03: Role-Based Access Control applied via Python.")

