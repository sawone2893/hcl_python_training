class Books:
  def __init__(self,price):
    self.price=price
  
  def __lt__(self,other):
    return self.price<other.price

b1=Books(400)
b2=Books(200)
print(b1<b2)