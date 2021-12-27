#!/usr/bin/env python

from setuptools import setup


setup(
    name='slugify',
    version='2.0.0',
    url='https://github.com/simplylizz/django-slugify',
    author="Anton Yanchenko",
    author_email="simplylizz@gmail.com",
    description="",
    license='BSD',
    platforms=['linux'],
    install_requires=[
        # not sure about exact version
        'django>=2.0.0',
        'unidecode',
    ],
)
