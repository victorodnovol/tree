from distutils.core import setup

setup(name='tree',
      version='1.0',
      description='System management script',
      author='Viktor',
      author_email='viktor.odnovol@gmail.com',
      packages=['lib', ''],
      package_dir={
          'lib': 'lib',
      },
      entry_points={
          'console_scripts': [
              'sysmanager = tree:SysManager',
          ],
      })
