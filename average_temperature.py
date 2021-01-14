class Country():
    def __init__(self, name, temp=None):
        if temp is None:
            temp = {}
        self.name = name
        self.temp = temp

    def toString(self):
        return ''.join([self.name, " => ", str(self.temp)])

    def addYear(self, year, temp):
        self.temp[year] = temp

    def coldestYear(self):
        return min(self.temp, key=self.temp.get)

    def hottestYear(self):
        return max(self.temp, key=self.temp.get)

    def output(self):
        return "".join([self.name, ' => ', self.coldestYear(), ",", self.hottestYear()])


def loadData(path):
    countries = []
    with open("results.txt") as f:
        header = f.readline()
        elements = header.split(" ")[:-1]
        for country in elements:
            countries.append(Country(country))

        for line in f:
            data = line.split(" ")[:-1]
            year = line.split()[-1]

            for i in range(len(data)):
                countries[i].addYear(year, data[i])
    return countries


if __name__ == "__main__":
    countries = loadData("results.txt")

#   DEBUG: dumps all the temperature data
#    for country in countries:
#        print(country.toString())

    for country in countries:
        print(country.output())
