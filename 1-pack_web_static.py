#!/usr/bin/python3
"""Compress web_static files."""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Compress the web_static directory."""
    if not os.path.exists("./versions/"):
        local("mkdir ./versions/")

    dt = datetime.now()
    command = "sudo tar -cvzf"
    result = local("{} ./versions/web_static_{}{}{}{}{}{}.tgz web_static"
                   .format(command,
                           dt.year,
                           dt.month,
                           dt.day,
                           dt.hour,
                           dt.minute,
                           dt.second),
                   capture=True)
    print(result.stdout)
