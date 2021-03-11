import unittest

from file_permission_hook import main


class TestMain(unittest.TestCase):
    def test_is_something_wrong(self):
        _paths = ["../test-sources/afile.txt"]
        self.assertEqual(main.is_something_wrong(_paths), True)


if __name__ == "__main__":
    unittest.main()
