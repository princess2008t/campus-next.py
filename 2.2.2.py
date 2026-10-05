class FavoriteAnimmal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age+=1
        return self.age

    def get_age(self):
        return self.age





a=FavoriteAnimmal("octavio",12)
print(a.get_age())
print(a.birthday())


b=FavoriteAnimmal("pppp",7)
print(b.get_age())
print(b.birthday())
