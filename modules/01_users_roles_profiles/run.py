import cx_Oracle

conn = cx_Oracle.connect("chrisorigi", "Myles003", "localhost:1539/FREEPDB1")
cur = conn.cursor()

# Create profile
cur.execute("""
BEGIN
    EXECUTE IMMEDIATE 'CREATE PROFILE secured_profiles
        LIMIT FAILED_LOGIN_ATTEMPTS 5
              PASSWORD_LIFE_TIME 90
              PASSWORD_REUSE_MAX 5';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -01920 THEN RAISE; END IF;
END;
""")

# Create role
cur.execute("""
BEGIN
    EXECUTE IMMEDIATE 'CREATE ROLE read_only_once';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -1921 THEN RAISE; END IF;
END;
""")

# Create user
cur.execute("""
BEGIN
    EXECUTE IMMEDIATE 'CREATE USER hruser IDENTIFIED BY Hr2025 PROFILE secured_profiles';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -01920 THEN RAISE; END IF;
END;
""")

# Grant role
cur.execute("GRANT read_only_once TO hruser")

# Grant object privileges
cur.execute("GRANT SELECT ON hr.employees TO read_only_once")

conn.commit()
cur.close()
conn.close()

print("Module 01: Users, Roles & Profiles applied via Python.")
