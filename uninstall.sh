#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root or use sudo."
  exit 1
fi

pip uninstall RFAccess --break-system-packages

if [ $? -eq 0 ]; then
  echo "RFAccess uninstalled successfully."
else
  echo "Failed to uninstall RFAccess. Please check for errors."
  exit 1
fi
