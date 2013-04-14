#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Ensure the version is correctly set in oscar.__init__.py
- Run: python setup.py sdist upload
"""

from setuptools import setup


setup(
    name='slugify',
    version='1.0.1',
    url='https://github.com/simplylizz/django-slugify',
    author="Anton Yanchenko",
    author_email="simplylizz@gmail.com",
    description="",
    license='BSD',
    platforms=['linux'],
    install_requires=[
        'django',
        'unidecode',
    ],
)
