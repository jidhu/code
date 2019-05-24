## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ?? A Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## A Dog has-a name
        self.name = name

## ?? A Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## ?? Person is-a object
class Person(object):

    def __init__(self, name):
        ## ?? Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ?? Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? Employee person has-a name
        super(Employee, self).__init__(name)
        ## ?? Employee has-a salary
        self.salary = salary

## ?? Fish is-a object
class Fish(object):
    pass

## ?? Salmon is-a Fish
class Salmon(Fish):
    pass

## ?? Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## ?? Frank has-a pet
frank.pet = rover

## ?? Flipper is-a Fish
flipper = Fish()

## ?? crouse is-a Salmon
crouse = Salmon()

## ?? Harry is-a Halibut
harry = Halibut()