#!/usr/bin/python3
"""Compress web_static files."""

from fabric.api import *
from datetime import datetime
import os
import sys

env.hosts = [
    '54.90.21.58',
    '54.144.46.194'
]
env.user   = "ubuntu"

def do_deploy(archive_path):
    """Deply the pack to the server."""
    if not os.path.exists(archive_path):
        return False


    result = put(archive_path, "/tmp/")
    if not result.succeeded:
        return False
    archive = archive_path.split("/")[-1]
    arch_name = archive.split(".")[0]
    release_path = "/data/web_static/releases/{}/".format(arch_name)
    if run("mkdir {}".format(release_path)) is True:
        return False
    result = run("tar -xzf /tmp/{} -C {}".format(archive, release_path))
    if not result.succeeded:
        return False

    result = run("rm /tmp/{}".format(archive))
    if not result.succeeded:
        return False
    result = run("rm /data/web_static/current")
    if not result.succeeded:
        return False
    result = run("ln -s {} /data/web_static/current".format(release_path))
    if not result.succeeded:
        return False

    return True
