import copy

class Animal:
    def __init__(self, name, number_of_legs, color):
        self.name = name
        self.number_of_legs = number_of_legs
        self.color = color

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogill', 0, 'paisley')
my_animals = [ harry, carrie, billy ]
more_animals = copy.copy(my_animals)
print(more_animals[0].name)
print(more_animals[1].name)

my_animals[0].name = 'ghoul'
print(my_animals[0].name)
print(more_animals[0].name)

sally = Animal('sphinx', 8, 'orange')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

more_animals = copy.deepcopy(my_animals)
my_animals[0].name = 'wyrm'
print(my_animals[0].name)
print(more_animals[0].name)
