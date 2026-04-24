class india():
    def country(self):
        print("india is a country")

    def language(self):
        print("india has many language")

    def culture(self):
        print("india has a rich culture")

class USA():
    def country(self):
        print("USA is a country")

    def language(self):
        print("USA has many language")

    def culture(self):
        print("USA has a rich culture")

ind = india()
usa = USA()
for con in (ind,usa):
    con.country()
    con.language()
    con.culture()