import unittest

from flaskr import util
class CompareTest(unittest.TestCase):
    def test_output(self):
        csv = util.load_csv()
        util.compare_tracks(csv[2], csv[3])
        self.assertNotEqual(0, 1)


if __name__ == "__main__":
    unittest.main()
