# class

class Person:
    # class attributes
    adress = 'no information'
    # constructor
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        # print('init metot')

    # instance methods
    def intro(self):
        print('Hello. I am '+ self.name)

    # instance methods
    def calculateAge(self):
        return 2022 - self.year

# object (instance)
p1 = Person(name='Alex', year=200)
p2 = Person(name='Ali', year=2005)

p1.intro()
p2.intro()

print(f'I am {p1.calculateAge()} years old')


# updating
# p1.name = 'Akar'

# accessing object attributes
# print(f'p1 :name: {p1.name} year: {p1.year} adress : {p1.adress}')
# print(f'p1 :name: {p2.name} year: {p2.year} adress : {p2.adress}')