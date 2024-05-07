from setuptools import find_packages
from setuptools import setup

setup(name = 'logging_example',
      description = 'Example use of logging.ini in a Python repository.',
      author = 'C Gosmeyer',
      url = 'https://github.com/cgosmeyer/logging_example',
      packages = find_packages(),
      install_requires = ['numpy', 'pandas'],
      include_package_data=True
)
