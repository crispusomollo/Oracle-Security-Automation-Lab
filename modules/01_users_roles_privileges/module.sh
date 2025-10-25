#!/bin/bash
# Module 01 - Users, Roles & Privileges
echo "[INFO] Executing Module 01: Users, Roles & Privileges"
sqlplus lab_admin/lab123 @create_users.sql
sqlplus lab_admin/lab123 @grant_privileges.sql
sqlplus lab_admin/lab123 @test_access.sql
echo "[INFO] Module 01 completed successfully."
