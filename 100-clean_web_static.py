#!/usr/bin/python3
"""clean up versions."""

import os
from fabric.api import *

env.hosts = ['18.204.5.64', '52.21.57.114']


def do_clean(number=0):
    """clean up old web static folders."""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    local_dir = 'versions/'
    remote_dir = '/data/web_static/releases/'
    archives = sorted(os.listdir('versions'))
    [archives.pop() for i in range(number)]
    for item in archives:
        local('rm {}{}'.format(local_dir, item))
    archives = run("ls -tr {}".format(remote_dir)).split()
    archives = [a for a in archives if "web_static_" in a]
    [archives.pop() for i in range(number)]
    [run("rm -rf {}{}".format(remote_dir, a)) for a in archives]
