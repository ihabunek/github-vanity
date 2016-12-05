#!/usr/bin/env python

from setuptools import setup

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name='github-vanity',
    version='0.1.0',
    description='Write to your GitHub activity chart',
    long_description=long_description,
    author='Ivan Habunek',
    author_email='ivan.habunek@gmail.com',
    url='https://github.com/ihabunek/github-vanity/',
    keywords='github vanity activity chart write',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['github_vanity'],
    install_requires=[
        'GitPython>=2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'vanity=github_vanity.console:main',
        ],
    }
)
