class Time:
  def __init__(self,h,m):
    self.h=h;
    self.m=m;
  
  def __add__(self,other):
    total_time1=self.h*60+self.m
    total_time2=other.h*60+other.m
    total_time=total_time1+total_time2
    hours=total_time//60
    min=total_time%60
    return (hours,min)

t1=Time(2,45)
t2=Time(3,25)
print(t1+t2)