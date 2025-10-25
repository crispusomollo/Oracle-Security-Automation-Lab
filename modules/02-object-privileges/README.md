# Module 02: Object Privileges

## 🎯 Objective

Learn to **grant, revoke, and manage object privileges** in Oracle. This ensures fine-grained access control for tables, views, sequences, and procedures.

---

## 🧩 Key Concepts

- Grant SELECT, INSERT, UPDATE, DELETE privileges on objects
- Revoke privileges when no longer needed
- Assign privileges via roles for easier management
- Enforce **least privilege principle**
- Automate privilege management using SQL, Bash, and Python

---

## ⚙️ Automation Scripts

### SQL Script::
```sql
-- Grant object privileges to a role
GRANT SELECT, INSERT ON employees TO read_only_role;

-- Grant object privileges directly to a user
GRANT UPDATE, DELETE ON employees TO hr_user;

-- Revoke privileges if needed
-- REVOKE DELETE ON employees FROM hr_user;
```
