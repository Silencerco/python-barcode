# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import setup, find_packages

exec(open('steenzout/barcode/version.py').read())


setup(
    name='steenzout.barcode',
    description='Python library for bar code generation.',
    author='Thorsten Weimann, Alexander Shorin, Pedro Salgado',
    author_email='kxepal@gmail.com,steenzout@ymail.com',
    version=__version__,
    maintainer='Pedro Salgado',
    maintainer_email='steenzout@ymail.com',
    url='https://github.com/steenzout/python-barcode/',
    namespace_packages=['steenzout'],
    packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
    package_data={
        '': [
            'LICENSE', 'NOTICE.md', 'README.md'],
        'steenzout.barcode': [
            'steenzout/barcode/fonts/*']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Graphics',
    ],
    install_requires=[
        str(pkg.req) for pkg in parse_requirements(
            'requirements.txt', session=pip.download.PipSession())],
    tests_require=[
        str(pkg.req) for pkg in parse_requirements(
            'test-requirements.txt', session=pip.download.PipSession())],
    license='MIT',
)
