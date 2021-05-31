class country:

    def home(self):
        print("Nepal")


class city(country):

    def __init__(self):
        super().home()
        print("Chitwan")


class municipality(city):

    def __init__(self):
        super().__init__()
        print("Ratnanagar")


st = municipality()
