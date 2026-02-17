#!/bin/bash

OS_NAME=$(uname)

if [ "$OS_NAME" = "Darwin" ]; then
  PROJECT_DIR="/Users/aboud/programming/retail-data-project"
else
  PROJECT_DIR="/home/aboud/programming/retail-data-project"
fi

cd $PROJECT_DIR 

. .venv/bin/activate

python ./alerts/mmafightstore.py
