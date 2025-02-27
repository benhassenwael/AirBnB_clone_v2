#!/usr/bin/python3
""" generate archive of web_static files """
from fabric import api
from datetime import datetime
import os


def do_pack():
    """ pack web_static files in .tgz file """
    with api.settings(warn_only=True):
        isdir = os.path.isdir('versions')
        if not isdir:
            mkdir = api.local('mkdir versions')
            if mkdir.failed:
                return None
        suffix = datetime.now().strftime('%Y%m%d%M%S')
        path = 'versions/web_static_{}.tgz'.format(suffix)
        tar = api.local('tar -cvzf {} web_static'.format(path))
        if tar.failed:
            return None
        size = os.stat(path).st_size
        print('web_static packed: {} -> {}Bytes'.format(path, size))
        return path
