import unittest

from flaskr import util
class CompareTest(unittest.TestCase):
    def test_output(self):
        csv = util.load_csv()
        util.compare_tracks(csv[1], csv[2])
        self.assertNotEqual(0, 1)


if __name__ == "__main__":
    unittest.main()
