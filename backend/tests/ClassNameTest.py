import unittest
import re

from flaskr import util


class ClassNameTest(unittest.TestCase):
    def test_all_names(self):
        data = util.load_csv()
        names = util.get_raw_classlist(data)
        for name in names:
            # ignore the numbers
            if re.match("\\d+", str(name)):
                continue
            self.assertNotEqual(util.get_name(name), "Error!", f'|{name} failed!|')


if __name__ == "__main__":
    unittest.main()
