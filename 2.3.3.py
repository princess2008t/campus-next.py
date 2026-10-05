class FavoriteAnimmal():
    count_animals = 0
    def __init__(self, age, name="octavio"):
        self._name = name
        self._age = age
        FavoriteAnimmal.count_animals += 1

    def set_name(self,new_name):
        self._name=new_name
        return self._name

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name



a=FavoriteAnimmal(12,)
print(a.get_age())
print(a.get_name())
print(a.set_name("sss"))


b = FavoriteAnimmal(5,"eee")
print(b.get_age())
print(b.get_name())
print(b.set_name("pppp"))

print(FavoriteAnimmal.count_animals)