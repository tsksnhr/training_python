class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name+" "+self.last_name

    def __str__(self):
        return self.last_name+","+self.first_name

person1 = Person("toshiki", "shinohara")
print(person1.first_name, person1.last_name)
print(person1.get_name())
print(person1)

person2 = Person()
person2.first_name = "ai"
person2.last_name = "xiao"
print(person2.first_name, person2.last_name)