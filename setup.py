#!/usr/bin/env python

from distutils.core import setup

setup(name='python-dabepg',
      version='0.5.0_spi31',
      description='Hybrid Radio SPI XML/binary implementation',
      author='Ben Poor',
      author_email='magicbadger@gmail.com',
      packages=['spi', 'spi.xml', 'spi.binary'],
      package_dir = {'' : 'src'}
)
