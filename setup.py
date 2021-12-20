#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bashunroll",
    version="0.1",
    author="Spencer Stingley",
    author_email="sstingle@usc.edu",
    description="A tool for unrolling bash scripts to return all commands executed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlankCanvasStudio/bash-unrolling",
    packages=setuptools.find_packages(),
    # entry_points={
    #     'console_scripts': [
    #         # migrating to pdb prefixes
    #         'script-name = module.foo.bar:main',
    #     ]
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires=['bashlex', 'bashparse'],
    test_suite='nose.collector',
    tests_require=['nose'],
)
