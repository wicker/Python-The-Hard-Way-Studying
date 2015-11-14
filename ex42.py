## Animal is-a class (object) of its own
class Animal(object):
	pass

## Dog is-a Animal which additionally has a name
class Dog(Animal):
	def __init__(self, name):
		self.name = name

## Cat is-a Animal which additionally (like Dog) has a name
class Cat(Animal):
	def __init__(self, name):
		self.name = name

## Person is-a class (object) of its own that has a name and pet
class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None

## Employee is-a Person who has a name and salary
## inherits the name from Person but doesn't have to explicitly refer to Person
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

## Fish is-a class (object) of its own
class Fish(object):
	pass

## Salmon and Halibut are Fishes
class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person who cares for Satan
mary = Person("Mary")
mary.pet = satan

## Frank is-an employee who makes 120K
frank = Employee("Frank",120000)
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse and Harry are particular kinds of fish
crouse = Salmon()
harry = Halibut()

