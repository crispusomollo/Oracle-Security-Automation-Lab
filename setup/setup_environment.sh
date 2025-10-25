#!/bin/bash
# setup_environment.sh - Configure Oracle environment variables
echo "[INFO] Configuring Oracle Environment..."
export ORACLE_SID=FREE
export ORACLE_HOME=/opt/oracle/product/23ai/dbhomeFree
export PATH=$ORACLE_HOME/bin:$PATH
echo "[INFO] Oracle environment configured successfully."
