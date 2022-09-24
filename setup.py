#!/usr/bin/env python3
"""Setup downloader-cli"""

import io
from setuptools import setup

with io.open("README.md", encoding='utf-8') as fh:
    long_description = fh.read()

requirements = [
    'urllib3>=1.25.6'
]

#exec(open("downloader_cli/__version__.py").read())


setup(
    name="downloader_cli",
    version=__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CS222-UIUC/course-project-group-13",
    packages=["downloader_cli"],
    classifiers=(
        [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
    ),
    entry_points={
        'console_scripts': [
            "dw = downloader_cli.download:main"
        ]
    },
    install_requires=requirements,
)
