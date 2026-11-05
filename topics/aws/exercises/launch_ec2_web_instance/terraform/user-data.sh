#!/bin/bash
set -euo pipefail
dnf install -y httpd
printf '%s\n' 'I made it! This is awesome!' > /var/www/html/index.html
systemctl enable --now httpd
