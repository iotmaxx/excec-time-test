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
    ]
)
