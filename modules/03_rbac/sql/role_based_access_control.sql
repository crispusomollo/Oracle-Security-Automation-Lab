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

