from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='gitube',
      version=version,
      description="Web interface for git repo manager.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='git',
      author='harryxu',
      author_email='harryzhxu@gmail.com',
      url='https://github.com/harryxu/gitube',
      license='bsd',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django>=1.3',
          'django-authopenid',
          'django-registration',
          'gitosis',
          'django-bootstrap-form',
      ],
      dependency_links = [
          'http://eagain.net/gitweb/?p=gitosis.git;a=snapshot;h=dedb3dc63f413ed6eeba8082b7e93ad136b16d0d;sf=tgz#egg=gitosis',
          'https://github.com/tzangms/django-bootstrap-form/tarball/master#egg=django-bootstrap-form',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
