#!/usr/bin/env python3

from setuptools import find_packages, setup

with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name='trod',
    version='0.0.1',
    license='BSD license',
    author='acthse',
    author_email='acthse@outlook.com',
    url='https://github.com/acthse/trod',
    description='Trod is a very simple asynchronous Python ORM based on asyncio',
    long_description=readme,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires='>=3.6',
    keywords='orm asyncio aiomysql python3 mysql',
    zip_safe=False,
    install_requires=[
        'aiomysql>=0.0.19',
    ],
)
