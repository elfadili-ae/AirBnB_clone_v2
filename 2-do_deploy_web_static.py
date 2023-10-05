#!/usr/bin/python3
"""Compress web_static files."""

from fabric.api import local
from fabric.api import run
from fabric.api import put
from fabric.api import env
from datetime import datetime
import os

env.hosts = [
    '54.90.21.58',
    '54.144.46.194'
]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Deply the pack to the server."""
    if not os.path.isfile(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive = archive_path.split("/")[-1]
        arch_name = archive.split(".")[0]
        release_path = "/data/web_static/releases/{}/".format(arch_name)
        run("mkdir -p {}".format(release_path))

        run("tar -xzf /tmp/{} -C {}".format(archive, release_path))
        run("rm /tmp/{}".format(archive))
        pth = "/data/web_static/releases"
        run("mv {}/{}/web_static/* {}/{}".format(pth, arch_name, pth, arch_name))

        run("rm -rf {}/{}/web_static".format(pth, arch_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True
    except Exception:
        return False
