#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root or use sudo."
  exit 1
fi

pip install -e . --break-system-packages

if [ $? -eq 0 ]; then
  echo "Package installed successfully."
else
  echo "Failed to install the package. Please check for errors."
  exit 1
fi