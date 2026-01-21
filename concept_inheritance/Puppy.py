from Dog import Dog

class Puppy(Dog):
  def __init__(self, name, type):
    super().__init__(name, type)
  
  def eat(self):
    print("Puppy eats meat")
  
  def speak(self):
    print("Puppy hushes!")