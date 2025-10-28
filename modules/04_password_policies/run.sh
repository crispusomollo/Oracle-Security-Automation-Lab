#!/bin/bash
ORACLE_USER="system"
ORACLE_PASS="oracle"
ORACLE_SID="ORCLCDB"

sqlplus -S $ORACLE_USER/$ORACLE_PASS@$ORACLE_SID <<EOF
@sql/password_policies.sql
EXIT
EOF

echo "Module 04: Password & Resource Policies applied successfully."

