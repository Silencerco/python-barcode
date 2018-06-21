# -*- coding: utf-8 -*-

import sys

import requirements

from setuptools import setup, find_packages

exec(open('steenzout/barcode/metadata.py').read())

PREFIX = 'py%s%s' % (sys.version_info.major, sys.version_info.minor)


def install_requires(file_name):
    """
    Parse the requirements.txt file

    Returns:
        list: parsed requirements.txt
    """
    required_packages = []
    with open(file_name, 'r') as f:
        for i in requirements.parse(f):
            if i.name:
                if i.editable: # has an -e at the beginning
                    required_packages.append(i.name)
                else:
                    required_packages.append(i.line)
    return required_packages


setup(
    name=__project__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    url=__url__,
    namespace_packages=['steenzout'],
    packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
    package_data={
        '': [
            'LICENSE', 'NOTICE.md', 'README.md'],
        'steenzout.barcode': [
            'fonts/*']
    },
    classifiers=__classifiers__,
    install_requires=install_requires('requirements.txt'),
    tests_require=install_requires('requirements-test.txt'),
    license=__license__,
    extras_require={
        'cli': install_requires('requirements-extra-cli.txt'),
        'image': install_requires('requirements-extra-image.txt'),
    },
    entry_points={
        'console_scripts':
            ['%s-barcode = steenzout.barcode.cli:cli' % PREFIX]
    }
)
