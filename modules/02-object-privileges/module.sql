#!/bin/bash
ORACLE_USER="system"
ORACLE_PASS="oracle"
ORACLE_SID="ORCLCDB"

sqlplus -S $ORACLE_USER/$ORACLE_PASS@$ORACLE_SID <<EOF
@module02.sql
EXIT
EOF

echo "Module 02: Object Privileges applied successfully."

