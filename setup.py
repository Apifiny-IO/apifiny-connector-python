#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   new_order.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''


import os
from setuptools import setup, find_packages

with open(
    os.path.join(os.path.dirname(__file__), "requirements.txt"), "r"
) as fh:
    requirements = fh.readlines()

NAME = "apifiny"
DESCRIPTION = (
    "This is a lightweight library that works as a connector to Apifiny OPEN API."
)
AUTHOR = "Apifiny"
URL = "https://github.com/Apifiny-IO/apifiny-connector-python"
VERSION = None

about = {}

with open("README.md", "r") as fh:
    about["long_description"] = fh.read()

root = os.path.abspath(os.path.dirname(__file__))

if not VERSION:
    with open(os.path.join(root, "apifiny", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    license="MIT",
    description=DESCRIPTION,
    long_description=about["long_description"],
    long_description_content_type="text/markdown",
    AUTHOR=AUTHOR,
    url=URL,
    keywords=["apifiny", "api", "unified APIs", "connect", "market data", "cryptocurrency", "tickdata", "spot", "futures", "orderbook data",
              "executed transactions data", "history market data", "real time market data", "fix protocol", "websocket api", "http api", "rest api", "fix api"],
    install_requires=[req for req in requirements],
    packages=find_packages(exclude=("tests",)),
    package_data = {'': ['*.yaml'],},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
