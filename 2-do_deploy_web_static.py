#!/usr/bin/python3
"""send web static files to remotes server."""

from fabric.api import *

env.hosts = ['18.204.5.64', '52.21.57.114']


def do_deploy(archive_path):
    """define a function to handle web static."""
    try:
        fn = archive_path.split('/')[1]
        dest_file = '/tmp/' + fn
        put(archive_path, dest_file)
        ef = fn.split('.')[0] # end file
        run('mkdir -p /data/web_static/releases/{}/'.format(ef))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(fn, ef))
        run('rm /tmp/{}'.format(fn))
        path = '/data/web_static/releases/{}/'.format(ef)
        run('mv {}web_static/* {}'.format(path, path))
        run('rm -rf {}web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        print('New version deployed!')
        return True
    except Exception:
        return False
