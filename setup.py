import os

from setuptools import setup, find_packages

from tiddlywebplugins.bfw import (__version__ as VERSION, __author__ as AUTHOR,
        __license__ as LICENSE, __doc__ as DESC)


META = {
    'name': 'tiddlywebplugins.bfw',
    'url': 'https://github.com/FND/tiddlywebplugins.bfw',
    'version': VERSION,
    'description': 'Barely Functioning Wiki',
    'long_description': DESC.strip(),
    'license': LICENSE,
    'author': AUTHOR,
    'author_email': '',
    'maintainer': 'FND',
    'packages': find_packages(exclude=['test']),
    'platforms': 'Posix; MacOS X; Windows',
    'include_package_data': False,
    'zip_safe': False,
    'install_requires': ['tiddlyweb', 'tiddlywebplugins.utils',
            'tiddlywebplugins.logout', 'tiddlywebplugins.templates'],
    'extras_require': {
        'testing': ['pytest', 'wsgi-intercept', 'httplib2'],
        'coverage': ['figleaf', 'coverage']
    }
}


if __name__ == '__main__':
    setup(**META)
