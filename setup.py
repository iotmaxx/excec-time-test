'''
    exec-time-test is a software to get the current load of a linux system.

    Copyright (C) 2025  IoTmaxx GmbH <info@iotmaxx.de>

    This file is part of exec-time-test.

    exec-time-test is free software: you can redistribute it and/or modify it under the terms of 
    the version 3 of the GNU General Public License as published by the Free Software Foundation.

    exec-time-test is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Foobar. If 
    not, see <https://www.gnu.org/licenses/>. 
'''
from setuptools import setup, find_packages

version = {}
with open("exec_time_test/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='exec_time_test',
    version=version['__version__'],
    url='https://github.com/iotmaxx/exec-time-test',
    author='Ralf Glaser',
    author_email='glaser@iotmaxx.de',
    description='get current CPU load, memory usage and execution time',
    packages=find_packages(),    
    install_requires=[
        argparse,
        psutil
    ]
)
