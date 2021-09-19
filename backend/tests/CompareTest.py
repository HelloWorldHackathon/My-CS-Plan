import unittest

from flaskr import util
class CompareTest(unittest.TestCase):
    def test_output(self):
        csv = util.load_csv()
        first = 7
        second = 6

        util.compare_tracks(csv[max(first, second)], csv[min(first, second)])
        self.assertNotEqual(2, 1)


if __name__ == "__main__":
    unittest.main()

