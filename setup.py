
from setuptools import setup, find_packages

setup(name='Bayesian optimisation',
      version='1.0.dev1',
      description='Bosch internal bayesian optimisation implementation',
      author='Anna Eivazi',
      author_email='anna.eivazi@de.bosch.com',
      url='TODO',
      platforms=['Windows', 'Linux'],
      python_requires='>=3.4',
      packages=find_packages(exclude=['tests'])
     )