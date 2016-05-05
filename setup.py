# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
"""
打包的用的setup必须引入，
"""

VERSION = '0.1.3'

setup(name='flask-admin.py',
      version=VERSION,
      description="copy from djang-admin.py",
      long_description='for easy flask Web',
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python flask flask-admin.py',
      author='konglx90',
      author_email='konglx90@gmail.com',
      url='https://github.com/konglx90/flask-admin.py',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        '',
      ],
      entry_points={
        'console_scripts':[
            'flask-admin.py = flask.admin:main'
        ]
      },
)