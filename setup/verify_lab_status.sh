#!/bin/bash
source ./setup_environment.sh
sqlplus / as sysdba <<EOF2
SELECT username, account_status FROM dba_users WHERE username='LAB_ADMIN';
EXIT;
EOF2
