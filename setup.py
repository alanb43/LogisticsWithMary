"""
Insta485 python package configuration.

Andrew DeOrio <awdeorio@umich.edu>

Adapted for LogisticsWithMary (business logistics web application)
    by Alan Bergsneider <bera@umich.edu>
"""

from setuptools import setup

setup(
    name='LogisticsWithMary',
    version='0.2.0',
    packages=['logisticswithmary'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'Flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
    ],
    python_requires='>=3.6',
)
