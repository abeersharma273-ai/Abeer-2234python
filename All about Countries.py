class India:
    def capital(self):
        print("Capital of India is New Delhi")

    def language(self):
        print("Most widely spoken language in India is Hindi")

    def type(self):
        print("India is a developing country")


class USA:
    def capital(self):
        print("Capital of USA is Washington, D.C.")

    def language(self):
        print("Most widely spoken language in USA is English")

    def type(self):
        print("USA is a developed country")


def show_info(country):
    country.capital()
    country.language()
    country.type()


for c in (India(), USA()):
    show_info(c)
    print()
