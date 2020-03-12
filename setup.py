# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()



setup(
    name='astroimages_fits',
    packages = ['astroimages_fits'],
    version='0.1',
    description='AstroImages - FITS files related routines and classes',
    long_description=readme,
    author='Rodrigo de Souza',
    author_email='rsouza01@gmail.com',
    url='https://github.com/AstroImages/astroimages-fits',
    download_url = 'https://github.com/AstroImages/astroimages-fits/archive/v_01.tar.gz',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'astropy',
        'numpy'
    ],    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)