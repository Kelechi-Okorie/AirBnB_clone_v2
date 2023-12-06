#!/usr/bin/python3
"""generates a .tgz archive fromt he contens of web_static folder"""

from fabric.operations import local
from datetime import datetime

def do_pack():
    """compresses contents of web_static folder"""

    now = datetime.now()
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(now, "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result