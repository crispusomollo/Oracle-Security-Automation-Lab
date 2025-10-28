# Module 03: Role-Based Access Control (RBAC)

## 🎯 Objective

Learn to implement **hierarchical roles and enforce least privilege** using Role-Based Access Control.  
RBAC centralizes permission management and simplifies user access control.

---

## 🧩 Key Concepts

- Hierarchical roles: admin, developer, read-only
- Grant roles to users for consolidated privileges
- Enforce **least privilege principle**
- Combine object and system privileges under roles
- Automate role assignment using SQL, Bash, and Python

---

## ⚙️ Automation Scripts

### SQL Script: `module03.sql`

```sql
-- Create hierarchical roles
CREATE ROLE admin_role;
CREATE ROLE dev_role;
CREATE ROLE read_only_role;

-- Assign object privileges to roles
GRANT SELECT, INSERT, UPDATE, DELETE ON employees TO dev_role;
GRANT SELECT ON employees TO read_only_role;

-- Grant system privileges to admin
GRANT CREATE USER, ALTER USER, DROP USER TO admin_role;

-- Assign roles to users
GRANT admin_role TO system_admin;
GRANT dev_role TO hr_user;
GRANT read_only_role TO analyst_user;

