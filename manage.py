#!/usr/bin/env python3
import os
import sys
import time

if __name__ == "__main__":
    # wait the database being ready (docker + docker-compose)
    time.sleep(2)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scanner.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
