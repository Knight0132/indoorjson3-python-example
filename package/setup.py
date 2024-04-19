"""
File Name: setup.py

Copyright (c) 2023 - 2024 IndoorJson

Author: Ziwei Xiang <knightzz1016@gmail.com>
Create Date: 2024/4/19
"""


from setuptools import setup, find_packages


setup(
    name='indoorjson3',
    version='0.1.0',
    package_dir={'': 'indoorjson3-python'},
    packages=find_packages(where='indoorjson3-python'),
    description='A Python package for IndoorJson project',
    author='Ziwei Xiang',
    author_email='knightzz1016@gmail.com',
    url='https://github.com/Knight0132/indoorjson3-python',
    install_requires=[
        'shapely',
        'typing',
        'numpy',
        'plotly'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
