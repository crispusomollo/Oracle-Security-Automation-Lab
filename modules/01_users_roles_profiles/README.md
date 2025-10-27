# Module 01: Users, Roles & Profiles

## 🎯 Objective

Learn to **create and manage Oracle database users, roles, and profiles**, enforce password policies, and set up secure access using automation scripts.

---

## 🧩 Key Concepts

- User creation and management
- Role creation and assignment
- Password and profile policies
- Least privilege principle
- Automation using SQL, Bash, and Python

---

## ⚙️ Automation Scripts

### 1️⃣ SQL Script: `module01.sql`

- Create users and roles
- Assign privileges
- Set password/profile policies

**Example Commands:**
```sql
-- Create profile
CREATE PROFILE secure_profile
  LIMIT
    FAILED_LOGIN_ATTEMPTS 5
    PASSWORD_LIFE_TIME 90
    PASSWORD_REUSE_MAX 5;

-- Create role
CREATE ROLE read_only_role;

-- Create user
CREATE USER hr_user IDENTIFIED BY "Hr@123"
  PROFILE secure_profile;

-- Grant role to user
GRANT read_only_role TO hr_user;

-- Grant object privileges
GRANT SELECT ON employees TO read_only_role;

