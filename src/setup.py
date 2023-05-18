"""Simple setup script for proconip package."""

from setuptools import setup, find_packages

install_requires = [
    "aiohttp>=3.8",
    "yarl>=1.8",
]

setup(name="proconip", version="0.0.2", packages=find_packages())
