import unittest
from average_temperature import Country, loadData


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

    def testExam(self):
        countries = loadData("results.txt")
        for country in countries:
            if country.name == "France":
                self.assertEqual("France => 1996,2018", country.output())
            elif country.name == "Sweden":
                self.assertEqual("Sweden => 2004,2017", country.output())
            elif country.name == "Germany":
                self.assertEqual("Germany => 2000,2017", country.output())


if __name__ == "__main__":
    unittest.main()
