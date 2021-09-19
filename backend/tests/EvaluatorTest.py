import unittest

from flaskr.evaluator import evaluate
from flaskr.util import format_schedule, get_name, load_csv


class EvaluatorTest(unittest.TestCase):
    def test_evaluator(self):
        data = load_csv()

        evaluated = evaluate(data[0], data[1])
        print(evaluated)
        print(list(map(format_schedule, evaluated)))


if __name__ == "__main__":
    unittest.main()
