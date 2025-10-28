-- Grant role to user
GRANT read_only_role TO hr_user;

-- Grant object privileges
GRANT SELECT ON employees TO read_only_role;
