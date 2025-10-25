#!/bin/bash
# init_lab.sh - Initialize Oracle Security Lab
set -e
LOG_FILE="../automation/logs/setup.log"
echo "[INFO] Starting lab setup..." | tee $LOG_FILE
source ./setup_environment.sh
sqlplus / as sysdba @create_lab_user.sql | tee -a $LOG_FILE
sqlplus lab_admin/lab123 @load_dummy_data.sql | tee -a $LOG_FILE
echo "[INFO] Lab setup completed successfully!" | tee -a $LOG_FILE
