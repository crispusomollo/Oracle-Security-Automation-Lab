import cx_Oracle
try:
    conn = cx_Oracle.connect("intruder/intruder123@localhost/FREE")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lab_admin.employees")
    print(cursor.fetchall())
except cx_Oracle.DatabaseError as e:
    print("[ALERT] Unauthorized access attempt detected!")
    print(e)
finally:
    try:
        conn.close()
    except:
        pass
