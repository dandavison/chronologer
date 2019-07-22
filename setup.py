import os

from setuptools import find_packages
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "README.md")) as fp:
    long_description = fp.read()


setup(
    name="chronologer",
    url="https://github.com/dandavison/chronologer",
    version="0.0.1",
    author="Dan Davison",
    author_email="dandavison7@gmail.com",
    description="Visualize changes in program timing over git commit history",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    entry_points={"console_scripts": ["chronologer = chronologer:main"]},
)
