from setuptools import setup, find_packages
import os

setup(
    name = "rfclient",
    version = "0.2",
    
    packages = find_packages('.'),
    package_dir = {'':'.'},
)
