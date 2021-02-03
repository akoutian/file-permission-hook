import unittest

from file_permission_hook import main


class TestMain(unittest.TestCase):
    def test_help(self):
        self.assertEqual(main.main(), 0)

if __name__ == "__main__":
    unittest.main()

