#!/usr/bin/python3
"""deploy full stack"""

import os
from fabric.api import *
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack

env.hosts = ['18.204.5.64', '52.21.57.114']


def deploy():
    """deploy full."""
    path = do_pack()
    if path is None:
        return False
    val = do_deploy(archive_path=path)
    return val
