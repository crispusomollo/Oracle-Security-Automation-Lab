import cx_Oracle

conn = cx_Oracle.connect("system", "oracle", "localhost/XEPDB1")
cur = conn.cursor()

# Create secure profile
cur.execute("""
BEGIN
    EXECUTE IMMEDIATE 'CREATE PROFILE secure_profile
        LIMIT FAILED_LOGIN_ATTEMPTS 5
              PASSWORD_LIFE_TIME 90
              PASSWORD_REUSE_MAX 5
              PASSWORD_LOCK_TIME 1
              SESSIONS_PER_USER 5
              CPU_PER_SESSION 10000
              CONNECT_TIME 60';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -01920 THEN RAISE; END IF;
END;
""")

# Assign profile to users
for user in ["hr_user", "analyst_user"]:
    cur.execute(f"ALTER USER {user} PROFILE secure_profile")

conn.commit()
cur.close()
conn.close()

print("Module 04: Password & Resource Policies applied via Python.")

