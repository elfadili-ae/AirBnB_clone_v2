#!/usr/bin/python3
"""Compress web_static files."""

from fabric.api import *
import os


env.hosts = [
    '54.90.21.58',
    '54.144.46.194'
]


def do_clean(number=0):
    """Clean up out of date archives."""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archs = sorted(os.listdir("versions"))
    [archs.pop() for i in range(number)]
    with lcd("versions/"):
        [local("rm ./{}".format(arch)) for arch in archs]

    with cd("/data/web_static/releases/"):
        archs = run("ls -tr").split()
        archs = [arch for arch in archs if "web_static_" in arch]
        [archs.pop() for i in range(number)]
        [run("rm -rf ./{}".format(arch)) for arch in archs]
