#!/usr/bin/python3
"""create the archive file."""

from fabric.api import *
from datetime import datetime as dt


@runs_once
def do_pack():
    """function to archive web static."""
    local('mkdir -p versions')
    the_time = dt.now().strftime('%Y%m%d%H%M%S')
    filename = 'versions/web_static_{}.tgz'.format(the_time)
    comd = local('tar -cvzf {} web_static'.format(filename))
    if comd is not None:
        return filename
    else:
        return None
