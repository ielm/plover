#!/usr/bin/env python2.6
# Copyright (c) 2010 Joshua Harlan Lifton.
# See LICENSE.txt for details.

from distutils.core import setup
from plover import __version__
from plover import __description__
from plover import __long_description__
from plover import __url__

setup(name='plover',
      version=__version__,
      description=__description__,
      long_description=__long_description__,
      url=__url__,
      license='GPL 2',
      author='Joshua Harlan Lifton',
      author_email='joshua.harlan.lifton@gmail.com',
      maintainer='Joshua Harlan Lifton',
      maintainer_email='joshua.harlan.lifton@gmail.com',
      package_dir={'plover':'plover'},
      packages=['plover', 'plover.machine', 'plover.dictionary'],
      package_data={'plover' : ['assets/*']},
      data_files=[('/usr/share/applications', ['application/Plover.desktop']),
                  ('/usr/share/pixmaps', ['plover/assets/plover_on.png']),],
      scripts=['application/plover'],
      requires=['serial', 'Xlib', 'wx'],
      platforms=['GNU/Linux'],
      classifiers=['Programming Language :: Python',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Development Status :: 3 - Alpha',
                   'Environment :: X11 Applications',
                   'Intended Audience :: End Users/Desktop',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Topic :: Adaptive Technologies',
                   'Topic :: Desktop Environment',]
      )
