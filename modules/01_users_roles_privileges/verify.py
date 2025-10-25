import cx_Oracle

conn = cx_Oracle.connect("system", "oracle", "localhost/XEPDB1")
cur = conn.cursor()

# Create profile
cur.execute("""
    BEGIN
        EXECUTE IMMEDIATE 'CREATE PROFILE secure_profile
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
        EXECUTE IMMEDIATE 'CREATE ROLE read_only_role';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -1921 THEN RAISE; END IF;
    END;
""")

# Create user
cur.execute("""
    BEGIN
        EXECUTE IMMEDIATE 'CREATE USER hr_user IDENTIFIED BY Hr@123 PROFILE secure_profile';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -01920 THEN RAISE; END IF;
    END;
""")

# Grant role
cur.execute("GRANT read_only_role TO hr_user")

# Grant object privileges
cur.execute("GRANT SELECT ON employees TO read_only_role")

conn.commit()
cur.close()
conn.close()

print("Module 01: Users, Roles & Profiles applied via Python.")

