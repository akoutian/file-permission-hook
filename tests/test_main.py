import unittest

from src import main


class TestMain(unittest.TestCase):
    def test_is_something_wrong(self):
        # TODO: this doesn't work, because this file has already been
        #       committed into the repo.
        _paths = ["test-sources/afile.txt"]
        self.assertEqual(main.is_something_wrong(_paths), True)


if __name__ == "__main__":
    unittest.main()
