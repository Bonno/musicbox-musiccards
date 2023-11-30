#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source $SCRIPT_DIR/venv/bin/activate
$SCRIPT_DIR/venv/bin/python $SCRIPT_DIR/box.py
