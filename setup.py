#!/usr/bin/env python

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyeventstore',
    author='Made.com',
    author_email='coders@made.com',
    packages=find_packages(),
    include_package_data=True,
    version='0.1',
    description="Python Eventstore Client",
    long_description=read('README.rst'),
    url='https://github.com/madedotcom/pyeventstore',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords=('eventstore', ),
    zip_safe=False,
    install_requires=[r for r in read("requirements.txt").split("\n") if r],
    entry_points={
            'console_scripts': [
                'escli = pyeventstore.escli:climain',
            ],
        }
)
