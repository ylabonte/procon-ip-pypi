"""Simple setup script for proconip package."""

from setuptools import setup, find_packages

install_requires = [
    "aiohttp>=3.9",
    "async-timeout>=4.0",
    "yarl>=1.9",
]

setup(name="proconip", version="1.4.0", packages=find_packages())
