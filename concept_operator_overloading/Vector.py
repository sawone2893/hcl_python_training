class Vector:
  def __init__(self, v):
       self.v = tuple(v)

  def __mul__(self, other):
    return Vector(x * other for x in self.v)

  def __str__(self):
        return f"{self.v}"

v=Vector((1,2))
print(str(v*9))