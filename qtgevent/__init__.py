# coding=utf8

__all__ = ['install']
__version__ = '0.1.1'


# Patchers

def patch_loop():
    from .loop import QtLoop
    from gevent.hub import Hub
    Hub.loop_class = QtLoop


def install():
    patch_loop()
