class location:
    country = "Nepal"

    def __init__(self, city):
        print(self.country)
        print(city)


class city(location):

    def __init__(self, city):
        super().__init__(city)

    def data(self):
        print(self.population)


ktm = city("Kathmandu")
ktm.population = 4000000
ktm.data()

print()

chi = city("Chitwan")
ktm.population = 3500000
ktm.data()
