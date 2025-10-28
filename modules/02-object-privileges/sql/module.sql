```sql
-- Grant object privileges to a role
GRANT SELECT, INSERT ON employees TO read_only_once;

-- Grant object privileges directly to a user
GRANT UPDATE, DELETE ON employees TO hr_user;

-- Revoke privileges if needed
-- REVOKE DELETE ON employees FROM hr_user;
