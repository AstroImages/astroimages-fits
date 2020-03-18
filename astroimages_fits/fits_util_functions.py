from astropy.io import fits
import os
import hashlib


def extract_metadata_from_fits_file(fits_file_path):
    hdulist = fits.open(fits_file_path)
    hdr = hdulist[0].header

    return {
        'id': hashlib.md5(fits_file_path).hexdigest(),
        'title': os.path.basename(fits_file_path),
        'description': fits_file_path,
        'path': fits_file_path,
        'primaryHDU': {
            'SIMPLE': hdr['EXTEND'],
            'BITPIX': hdr['BITPIX'],
            'NAXIS': hdr['NAXIS'],
            'EXTEND': hdr['EXTEND']
        }
    }
    