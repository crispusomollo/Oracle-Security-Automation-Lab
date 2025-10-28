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

-- Assign profile to users
ALTER USER hr_user PROFILE secure_profile;
ALTER USER analyst_user PROFILE secure_profile;

-- Optional: check profile settings
SELECT * FROM DBA_PROFILES WHERE PROFILE='SECURE_PROFILE';

