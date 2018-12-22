import unittest

class Test_Game_Mechanics(unittest.TestCase):

    def test_trivial_statements(self):
        self.assertEqual(1, 1)
        self.assertEqual(2+2, 4)
        self.assertEqual(True, 1 == 1)