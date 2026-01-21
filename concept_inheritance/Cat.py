from inheritance.Animal import Animal

class Cat(Animal):
  def __init__(self, name, type):
    super().__init__(name, type)
  
  def eat(self):
   print("Eat milk")
  
  def speak(self):
   print("Cat meow!")