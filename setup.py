# encoding: utf-8

from distutils.core import setup

setup(
    name="qtgevent",
    version="0.1",
    description="PyQt4/5 backend for gevent",
    author="Matias Guijarro, Nauel Defossé",
    package_dir={
        "qtgevent": "qtgevent"
    },
    packages=["qtgevent"]
)
