import os
import django

from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()
execute_from_command_line("main.py runserver 127.0.0.1:8000".split())
