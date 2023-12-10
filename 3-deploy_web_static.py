#!/usr/bin/python3
"""generates and distributes an archive to my web servers"""

from fabric.operations import local, run, put
from fabric.api import env
import re
from datetime import datetime
import os


env.hosts = ['54.90.42.30', '100.26.153.218']


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


def do_deploy(archive_path):
    """distributes an archive to my web servers"""

    if not os.path.exists(archive_path):
        return False
    regex = r'^versions/(\S+).tgz'
    match = re.search(regex, archive_path)
    filename = match.group(1)
    result = put(archive_path, "/tmp{}.tgz".format(filename))
    if result.failed:
        return False
    result = run("mkdir -p /data/web_static_releases/{}/".format(filename))
    if result.failed:
        return False
    result = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                 .format(filename, filename))
    if result.failed:
        return False
    result = run("rm /tmp/{}.tgz".format(filename))
    if result.failed:
        return False
    result = run("mv /data/web_static/releases/{}"
                 "/web_static/* /data/web_static/releases/{}/"
                 .format(filename, filename))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/{}/web_static"
                 .format(filename))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                 .format(filename))
    if result.failed:
        return False
    print("New version deployed!")
    return True

def deploy():
    """distributing an archive to the web server"""

    path = do_pack()
    if path is None:
        return False
    result = do_deploy(path)
    return result