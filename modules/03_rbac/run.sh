#!/bin/bash
ORACLE_USER="system"
ORACLE_PASS="oracle"
ORACLE_SID="ORCLCDB"

sqlplus -S $ORACLE_USER/$ORACLE_PASS@$ORACLE_SID <<EOF
@sql/role_based_access_control.sql
EXIT
EOF

echo "Module 03: Role-Based Access Control applied successfully."

