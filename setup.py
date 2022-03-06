"""
Insta485 python package configuration.

Andrew DeOrio <awdeorio@umich.edu>

Taken for LogisticsWithMary (business logistics web application)
    by Alan Bergsneider <bera@umich.edu>
"""

from setuptools import setup

setup(
    name='LogisticsWithMary',
    version='0.1.0',
    packages=['LogisticsWithMary'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
        'selenium',
    ],
    python_requires='>=3.6',
)
