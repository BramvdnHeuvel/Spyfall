import unittest

from flask import jsonify

class Test_Game_Mechanics(unittest.TestCase):

    def test_trivial_statements(self):
        self.assertEqual(1, 1)
        self.assertEqual(2+2, 4)
        self.assertEqual(True, 1 == 1)
    
    def test_flaskproperties(self):
        self.assertEqual(1, 1)
        self.assertEqual(2+2, 4)
        self.assertEqual(True, 1 == 1)

        self.assertEqual(jsonify(1, 2, 3), jsonify([1, 2, 3]))
        self.assertEqual(jsonify({"a": 5, "b": 6}), jsonify(a=5, b=6))
