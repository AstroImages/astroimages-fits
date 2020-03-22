import unittest

import astroimages_fits.fits_test_util_functions as ftuf


class TestUtilFunctions(unittest.TestCase):

    def setUp(self):
        self.folders_per_layer = 3
        self.files_per_folder = 10
        self.temp_folder = '/home/rsouza/Projects/AstroImages/'

    def test_create_empty_fits_files_on_temp_folder(self):

        temp_folder, files_list = ftuf.create_empty_fits_files_on_temp_folder(self.files_per_folder)

        self.assertEqual(len(files_list), self.files_per_folder)

        temp_folder.cleanup()

    def test_create_empty_fits_files_on_path(self):

        temp_folder, files_list = ftuf.create_empty_fits_files_on_temp_folder(
            self.files_per_folder, self.temp_folder)

        self.assertEqual(len(files_list), self.files_per_folder)

        temp_folder.cleanup()


if __name__ == '__main__':
    unittest.main()
