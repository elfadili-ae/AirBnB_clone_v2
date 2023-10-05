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


def do_pack():
    """Compress the web_static directory."""
    if not os.path.exists("./versions/"):
        local("mkdir ./versions/")

    dt = datetime.now()
    command = "sudo tar -cvzf"
    arch = "web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                dt.month,
                                                dt.day,
                                                dt.hour,
                                                dt.minute,
                                                dt.second)
    try:
        local("{} ./versions/{} web_static".
              format(command, arch), capture=True)
        print(result.stdout)
        return new_archive
    except Exception:
        return None


def do_deploy(archive_path):
    """Deply the pack to the server."""
    if not os.path.isfile(archive_path):
        return False

    result = put(archive_path, "/tmp/")
    if not result.succeeded:
        return False
    archive = archive_path.split("/")[-1]
    arch_name = archive.split(".")[0]
    release_path = "/data/web_static/releases/{}/".format(arch_name)
    result = run("mkdir -p {}".format(release_path))
    if not result.succeeded:
        return False
    result = run("tar -xzf /tmp/{} -C {}".format(archive, release_path))
    if not result.succeeded:
        return False

    result = run("rm /tmp/{}".format(archive))
    if not result.succeeded:
        return False
    pth = "/data/web_static/releases"
    result = run("mv {}/{}/web_static/* {}/{}".
                 format(pth, arch_name, pth, arch_name))
    if not result.succeeded:
        return False
    result = run("rm -rf {}/{}/web_static".format(pth, arch_name))
    if not result.succeeded:
        return False
    result = run("rm -rf /data/web_static/current")
    if not result.succeeded:
        return False
    result = run("ln -s {} /data/web_static/current".format(release_path))
    if not result.succeeded:
        return False
    print("New version deployed!")
    return True


def deploy():
    """Deploy archive to the servers."""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
