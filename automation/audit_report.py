import cx_Oracle, csv, os
os.makedirs("automation/logs", exist_ok=True)
conn = cx_Oracle.connect("sys/oracle@localhost/FREE", mode=cx_Oracle.SYSDBA)
cursor = conn.cursor()
cursor.execute("SELECT username, action_name, obj_name, timestamp FROM dba_audit_trail ORDER BY timestamp DESC")
with open("automation/logs/audit.log", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["USERNAME", "ACTION", "OBJECT", "TIMESTAMP"])
    for row in cursor:
        writer.writerow(row)
print("[INFO] Audit log written to automation/logs/audit.log")
