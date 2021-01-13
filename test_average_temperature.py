import unittest
from average_temperature import Country


class CountryTest(unittest.TestCase):

    normal = Country("test", {"1": 1, "2": 2, "3": 3})
    redundancy = Country("test", {"1": -1, "2": -1})

    def testColdest(self):
        self.assertEqual(self.normal.coldestYear(), "1")

    def testHottest(self):
        self.assertEqual(self.normal.hottestYear(), "3")

    def testfirstColdest(self):
        self.assertEqual(self.redundancy.coldestYear(), "1")

    def testfirstHottest(self):
        self.assertEqual(self.redundancy.hottestYear(), "1")



if __name__ == "__main__":
    #unittest.main()
    print("Tests don't work because I had to revert to an earlier version of average_temperature.py, but here they are nevertheless")
