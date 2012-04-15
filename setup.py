from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='gitube',
      version=version,
      description='Gitube is a simple git repository management web application can be deployed on your own server.',
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='git',
      author='harryxu',
      author_email='harryzhxu@gmail.com',
      url='https://github.com/harryxu/gitube',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django>=1.4',
          'django-authopenid',
          'django-registration',
          'django-bootstrap-form',
      ],
      dependency_links = [
          'https://github.com/tzangms/django-bootstrap-form/tarball/master#egg=django-bootstrap-form',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
