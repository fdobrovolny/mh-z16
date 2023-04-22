"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_namespace_packages


# The version of this tool is based on the following steps:
# https://packaging.python.org/guides/single-sourcing-package-version/
VERSION = {}

with open("./src/mh_zxx/version.py") as fp:
    # pylint: disable=W0122
    exec(fp.read(), VERSION)

setup(
    name="mh_zxx",
    author="Filip Dobrovolny",
    author_email="dobrovolny.filip@gmail.com",
    url="https://github.com/fdobrovolny/mh-zxx",
    description="Python library for interaction with MH-Z16, MH-Z19 and similar.",
    version=VERSION.get("__version__", "0.0.0"),
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", exclude=["tests"]),
    install_requires=[
        "setuptools>=45.0",
        "pyserial>=3.5",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
        "Topic :: System :: Hardware",
    ],
)
