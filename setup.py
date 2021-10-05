from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.5'
DESCRIPTION = 'GLS Model to Python'
LONG_DESCRIPTION = 'A package that allows easier interfacing with Albion.'

# Setting up
setup(
    name="gls_python",
    version=VERSION,
    author="GLS",
    author_email="<gls@gls.co.za>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Engineers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)