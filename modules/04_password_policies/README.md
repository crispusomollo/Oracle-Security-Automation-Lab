# Module 04: Password & Resource Policies

## 🎯 Objective
Implement **secure password and resource policies** to enforce authentication security, account lockouts, and resource limits in Oracle.

---

## 🧩 Key Concepts

- Password complexity and expiration
- Account lockout after failed login attempts
- Resource limits: CPU, sessions, connect time
- Profiles to consolidate password and resource policies
- Automation using SQL, Bash, and Python

---

## ⚙️ Automation Scripts

### 1️⃣SQL Script: `module04.sql`

```sql
-- Create secure profile
CREATE PROFILE secure_profile
  LIMIT
    FAILED_LOGIN_ATTEMPTS 5
    PASSWORD_LIFE_TIME 90
    PASSWORD_REUSE_MAX 5
    PASSWORD_LOCK_TIME 1
    SESSIONS_PER_USER 5
    CPU_PER_SESSION 10000
    CONNECT_TIME 60;

-- Assign profile to user
ALTER USER hr_user PROFILE secure_profile;
ALTER USER analyst_user PROFILE secure_profile;

-- Optional: check profile settings
SELECT * FROM DBA_PROFILES WHERE PROFILE='SECURE_PROFILE';

