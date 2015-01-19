#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-disqus',
    version='0.5',
    description='Export comments and integrate DISQUS into your Django website',
    author='Emmanuelle Delescolle',
    author_email='emma@lasolution.be',
    url='https://github.com/nanuxbe/django-disqus/commits/master',
    license='New BSD License',
    classifiers=[
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python',
    ],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)
