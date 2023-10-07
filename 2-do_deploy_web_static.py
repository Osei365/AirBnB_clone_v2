#!/usr/bin/python3
"""send web static files to remotes server."""
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['localhost', '18.204.5.64', '52.21.57.114']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """define a function to handle web static."""
    if os.path.exists(archive_path) is False:
        return False
    fn = archive_path.split('/')[-1]
    dest_file = '/tmp/' + fn
    ef = fn.split('.')[0]  # end file
    path = '/data/web_static/releases/{}/'.format(ef)

    if put(archive_path, dest_file).failed:
        return False
    if run('mkdir -p {}'.format(path)).failed:
        return False
    if run('tar -xzf /tmp/{} -C {}'.format(fn, path)).failed:
        return False
    if run('rm /tmp/{}'.format(fn)).failed:
        return False
    if run('mv {}web_static/* {}'.format(path, path)).failed:
        return False
    if run('rm -rf {}web_static'.format(path)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s {} /data/web_static/current'.format(path)).failed:
        return False
    print('New version deployed!')
    return True
