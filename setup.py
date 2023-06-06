from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in siteshare/__init__.py
from siteshare import __version__ as version

setup(
	name="siteshare",
	version=version,
	description="Manage users and subscriptions on a single frappe site",
	author="Bantoo",
	author_email="devs@thebantoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
