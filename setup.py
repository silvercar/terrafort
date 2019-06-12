import os

from setuptools import setup, find_packages

install_requires = [
    'boto3',
    'click',
    'jinja2'
]

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='terrafort',
    version='0.2.0',
    install_requires=install_requires,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    long_description=read('README.md'),
    include_package_data=True,
    package_data={'terrafort': ['templates/*']},
    entry_points={
        'console_scripts': {
            'terrafort = terrafort.main:cli'
        }
    }
)
