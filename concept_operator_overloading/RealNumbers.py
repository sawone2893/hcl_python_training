class RealNumbers:
  def __init__(self,real,img):
    self.real=real
    self.img=img
  
  def __add__(self,other):
    total_real=self.real+other.real
    total_img=self.img+other.img
    return RealNumbers(total_real,total_img)
  
  def __str__(self):
    return f"{self.real} + {self.img}i"

rn1=RealNumbers(1,3)
rn2=RealNumbers(4,3)
print(rn1+rn2)

