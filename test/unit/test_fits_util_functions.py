from astropy.io import fits


import unittest

import tempfile
from astroimages_fits.fits_util_functions import extract_metadata_from_fits_file

class TestUtilFunctions(unittest.TestCase):

    def setUp(self):
        self.folders_per_layer = 3
        self.files_per_folder = 10

    def test_extract_metadata_from_fits_file(self):

        self.assertEqual(1, 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()

