from inheritance.Animal import Animal


class Dog(Animal):
  def __init__(self, name, type):
    super().__init__(name, type)
  
  def speak(self):
    print("Dog barks")
  
  def eat(self):
    print("Dog eats bone")