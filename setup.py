"""Use the following command to install retriever: python setup.py install"""

from setuptools import setup
import platform

p = platform.platform().lower()
extra_includes = []
if "darwin" in p:
    import py2app
    extra_includes = []
elif "win" in p:
    import py2exe
    import sys
    extra_includes = ['pyodbc', 'inspect']
    sys.path.append("C:\\Windows\\winsxs\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_bcb86ed6ac711f91")
from __init__ import VERSION


def clean_version(v):
    if v == 'master':
        return '1.0.0'
    return v.replace('v', '').replace('.rc', '').replace('.beta', '')

packages = [
            'retriever.lib',
            'retriever.engines',
            'retriever.app',
            'retriever',
            ]

try:
    import pymysql
    mysql_module = 'pymysql'
except ImportError:
    try:
        import MySQLdb
        mysql_module = 'MySQLdb'
    except ImportError:
        mysql_module = 'pymysql'

includes = [
            'xlrd',
            'wx',
            mysql_module,
            'psycopg2',
            'sqlite3',
            ] + extra_includes
            
excludes = [
            'pyreadline',
            'doctest',
            'optparse',
            'getopt',
            'pickle',
            'calendar',
            'pdb',
            'inspect',
            'email',
            'pywin', 'pywin.debugger',
            'pywin.debugger.dbgcon',
            'pywin.dialogs', 'pywin.dialogs.list',
            'Tkconstants', 'Tkinter', 'tcl',
            ]


setup(name='retriever',
      version=clean_version(VERSION),
      description='EcoData Retriever',
      author='Ben Morris',
      author_email='ben.morris@weecology.org',
      url='http://www.ecologicaldata.org/database-toolkits',
      packages=packages,
      package_dir={
                'retriever':''
                },
      entry_points={
        'console_scripts': [
            'retriever = retriever.main:main',
        ],
      },

      # py2exe flags
      windows = [{'script': "main.py",
                  'dest_base': "retriever",
                  'icon_resources':[(1,'icon.ico')]
                  }],
      zipfile = None,

      # py2app flags
      app=['main.py'],
      data_files=[],
      setup_requires=['py2app'],

      # options
      options = {'py2exe': {'bundle_files': 1,
                            'compressed': 2,
                            'optimize': 2,
                            'packages': packages,
                            'includes': includes,
                            'excludes': excludes,
                            },
                 'py2app': {'packages': packages,
                            'includes': includes,
                            'site_packages': True,
                            'resources': [],
                            'optimize': 2,
                            'argv_emulation': True,
                            'no_chdir': True,
                            },
                },
      )


try:
    from compile import compile
    compile()
except:
    pass
