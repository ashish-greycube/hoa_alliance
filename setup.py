from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in hoa_alliance/__init__.py
from hoa_alliance import __version__ as version

setup(
	name='hoa_alliance',
	version=version,
	description='Customization for House Owner Association business',
	author='GreyCube Technologies',
	author_email='admin@greycube.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
