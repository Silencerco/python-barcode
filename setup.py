# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import setup, find_packages

exec(open('steenzout/barcode/metadata.py').read())


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
            'steenzout/barcode/fonts/*']
    },
    classifiers=__classifiers__,
    install_requires=[
        str(pkg.req) for pkg in parse_requirements(
            'requirements.txt', session=pip.download.PipSession())],
    tests_require=[
        str(pkg.req) for pkg in parse_requirements(
            'requirements-test.txt', session=pip.download.PipSession())],
    license=__license__,
)
