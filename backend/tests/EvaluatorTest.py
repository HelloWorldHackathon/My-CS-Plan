import unittest

from flaskr.evaluator import evaluate
from flaskr.util import load_csv


class EvaluatorTest(unittest.TestCase):
    def test_evaluator(self):
        data = load_csv()

        print(evaluate(data[1], data[0]))


if __name__ == "__main__":
    unittest.main()
