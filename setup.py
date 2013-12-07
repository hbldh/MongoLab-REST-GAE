# -*- coding: utf-8 -*-
"""
:mod:`setup.py` -- NMMLib Setup file
======================================

.. module:: setup
   :platform: Unix, Windows
   :synopsis: The Python Packaging setup file for NMMLib.

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2013-09-14, 19:31

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from distutils.core import setup

setup(
      name='mongolab-rest-gae',
      version='0.1.0',
      description='A Python REST client for using MongoLab storage in Google App Engine.',
      author='Henrik Blidh',
      author_email='henrik.blidh@nedomkull.com',
      license='Nedomkull Mathematical Modeling',
      url='www.nedomkull.com',
      packages=[
                'mongolab-rest-gae',
                ],
      package_data={},
      install_requires=[],
      dependency_links=[],
      ext_modules=[],
      )

