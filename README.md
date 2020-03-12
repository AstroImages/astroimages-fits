AstroImages FITS Handling routines (astroimages-fits)
=================================

![Publish AstroImage-FITS Package](https://github.com/AstroImages/astroimages-fits/workflows/Publish%20AstroImage-FITS%20Package/badge.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)


FITS routines and wrappers


Usage
-----

Clone the repo:

    git clone https://github.com/AstroImages/astroimages-fits/
    cd astroimages-fits

Create virtualenv:

    virtualenv -p python3 env
    source env/bin/activate
    pip3 install -r requirements.txt


## Testing

To run unit tests:

    python -m unittest discover test/unit -v


## Packaging

To package
    
    python setup.py sdist

To upload

    pip3 install twine
    twine upload dist/*


## References

### Python Packaging
- https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

License
-------

MIT, see LICENSE file


