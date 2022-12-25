
# Inheritance (Kalıtım) : Miras alma

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname


    def who_am_i(self):
        print('I am a person')

class Student(Person):
   def __init__(self, fname, lname, number):
       Person.__init__(self, fname, lname)
       self.studentNumber = number


   # override
   def who_am_i(self):
       print('I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher.')


p1 = Person('Ali', 'Yılmaz')
s1 = Student('Çınar', 'Turan', 8051)
t1 = Teacher('Veli', 'Can', 'Math')

t1.who_am_i()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))
print(t1.firstName + ' ' + t1.lastName + ' ' + t1.branch)