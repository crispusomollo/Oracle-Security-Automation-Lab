#!/bin/bash
MODULE=$1
if [ -z "$MODULE" ]; then
  echo "Usage: ./run_module.sh <module_folder>"
  exit 1
fi
echo "[INFO] Running module: $MODULE"
cd ../modules/$MODULE
bash module.sh
