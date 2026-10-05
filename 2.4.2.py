class BigThing():
    def __init__(self, var):
        self.var = var

    def size(self):
        if type(self.var) == int:
            return self.var
        else:
            return len(self.var)


class BigCat(BigThing):
    def __init__(self, var, weight):
        BigThing.__init__(self, var)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "very fat"
        if self.weight > 15:
            return "fat"
        return "OK"


my_thing = BigThing("balloon")
my_thing1 = BigThing(33)

print(my_thing.size())
print(my_thing1.size())

cutie = BigCat("mitzy", 22)
print(cutie.size())