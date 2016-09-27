from setuptools import setup, find_packages
from pystt import __version__

setup(
    name='pystt',
    version=__version__,
    packages=find_packages(),
    description='pystt is the serialization and de-serialization library of STT.',
    url='https://github.com/dust8/pystt',
    license='MIT',
    keywords='pystt stt serialization de-serialization douyu')
