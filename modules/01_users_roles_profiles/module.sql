-- Create secure profile
CREATE PROFILE secure_profile
  LIMIT
    FAILED_LOGIN_ATTEMPTS 5
    PASSWORD_LIFE_TIME 90
    PASSWORD_REUSE_MAX 5;

-- Create a role
CREATE ROLE read_only_role;

-- Create user
CREATE USER hr_user IDENTIFIED BY "Hr@123"
  PROFILE secure_profile;

-- Grant role to user
GRANT read_only_role TO hr_user;

-- Grant object privileges
GRANT SELECT ON employees TO read_only_role;

