#!/usr/bin/env python

from distutils.core import setup
import queues
setup(name='queues',
      version='0.3',
      description='A lowest-common-denominator API for interacting with lightweight queue services.',
      author='Matt Croydon',
      author_email='mcroydon@gmail.com',
      url='http://code.google.com/p/queues/',
      packages=['queues', 'queues.backends'],
      py_modules=['test'],
      package_dir={'queues': 'queues'},
     )
