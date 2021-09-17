Process:

// Install this to be able to install gls_python and shapely
py -m pip install wheel

// install these, optional
py -m pip install geos
py -m pip install numpy
py -m pip install matplotlib
py -m pip install seaborn

// Open command prompt in the location where you pulled the repo
// There should be a setup.py file in there
// Once there run the following
py setup.py sdist bdist_wheel

// If should create a .whl file in a dist folder
// open a command prompt in this folder and run the following
py -m pip install gls_python-VERSION_NUMBER-py3-none-any.whl


// Shapely needs to be installed, the normal pip install didn't work from me
// Download the the .whl from from this site and install manually

Get the latest shapely for your pc from
https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely
Currently using Shapely‑1.7.1‑cp39‑cp39‑win32.whl
download and then pip install:

py -m pip install Shapely‑1.7.1‑cp39‑cp39‑win32.whl