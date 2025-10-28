-- Create secure profile
CREATE PROFILE secured_profile
  LIMIT
    FAILED_LOGIN_ATTEMPTS 5
    PASSWORD_LIFE_TIME 90
    PASSWORD_REUSE_MAX 5;

-- Create a role
CREATE ROLE read_only_role;
