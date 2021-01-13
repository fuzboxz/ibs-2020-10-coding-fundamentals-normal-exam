import unittest
from unique import uniq


class testUniq(unittest.TestCase):

    def test1(self):
        self.assertEqual(["g", "m", "n", "r"], uniq("anagram"))

    def test2(self):
        self.assertEqual([], uniq("aaaaaaaa"))


if __name__ == "__main__":
    unittest.main()
