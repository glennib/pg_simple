import os
import codecs

from setuptools import setup, find_packages

try:
    with open(os.path.abspath('./README.rst')) as stream:
        long_description = stream.read()
except:
    long_description = 'pg_simple is a simple wrapper for Python psycopg2 with connection pooling'

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
    
setup(
    name="pg_simple",
    version=get_version("pg_simple/__init__.py"),
    packages=find_packages(),
    install_requires=['psycopg2-binary'],
    classifiers=['Topic :: Database',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Development Status :: 3 - Alpha'],
    author='Masroor Ehsan Choudhury',
    author_email='masroore@gmail.com',
    description='A simple wrapper for Python psycopg2 with connection pooling',
    long_description=long_description,
    license='BSD',
    keywords='psycopg2 postgresql sql database',
    url='https://github.com/masroore/pg_simple',
)
