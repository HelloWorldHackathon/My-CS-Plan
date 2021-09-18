import unittest

from flaskr.util import load_csv
from flaskr.evaluator import evaluate

class EvaluatorTest(unittest.TestCase):
    def test_evaluator(self):
        data = load_csv()

        print(data[0])

        evaluate(data[0], data[1])
        pass


if __name__ == "__main__":
    unittest.main()
